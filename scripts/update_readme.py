import os
import re
import json

def get_difficulty_badge(diff):
    diff_lower = (diff or '').strip().lower()
    if diff_lower == 'easy':
        return '<img src="https://img.shields.io/badge/Easy-22c55e?style=flat-square&logoColor=white" alt="Easy"/>'
    elif diff_lower == 'medium':
        return '<img src="https://img.shields.io/badge/Medium-f59e0b?style=flat-square&logoColor=white" alt="Medium"/>'
    elif diff_lower == 'hard':
        return '<img src="https://img.shields.io/badge/Hard-ef4444?style=flat-square&logoColor=white" alt="Hard"/>'
    return diff

def get_language_name(ext):
    ext_map = {
        '.cpp': 'C++',
        '.c': 'C',
        '.py': 'Python',
        '.java': 'Java',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust'
    }
    return ext_map.get(ext, ext[1:].upper() if ext.startswith('.') else ext)

def parse_topics_from_readme(readme_content):
    topics_map = {}
    topic_section = re.search(r'<!---LeetCode Topics Start-->(.*?)<!---LeetCode Topics End-->', readme_content, re.DOTALL)
    if not topic_section:
        return topics_map
    
    current_topic = None
    for line in topic_section.group(1).splitlines():
        line = line.strip()
        if not line:
            continue
        
        # Match headers: ### 🔹 Array or ## Array or ## Hash Table
        header_match = re.match(r'^(?:#+)\s*(?:[^\w\s]*\s*)?([A-Za-z0-9\s&,/-]+)', line)
        if header_match and not line.startswith('|') and not line.startswith('- ['):
            clean_hdr = header_match.group(1).strip()
            if clean_hdr:
                current_topic = clean_hdr
                continue

        # Match links: - [0001 - Two Sum](./0001-two-sum) or | [0001-two-sum](...) |
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', line)
        for link_text, link_target in links:
            if current_topic:
                # Extract identifiers from link_text and link_target
                target_slug = link_target.rstrip('/').split('/')[-1].lower()
                text_slug = re.sub(r'^[0-9]+\s*[-–:]\s*', '', link_text).strip().lower().replace(' ', '-')
                
                for key in [target_slug, text_slug, link_text.strip().lower()]:
                    if key not in topics_map:
                        topics_map[key] = set()
                    topics_map[key].add(current_topic)
                    
                    # Also match 4-digit problem number
                    num_match = re.search(r'(\d{4})', key)
                    if num_match:
                        num_key = num_match.group(1)
                        if num_key not in topics_map:
                            topics_map[num_key] = set()
                        topics_map[num_key].add(current_topic)

    return topics_map

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    readme_path = os.path.join(repo_root, 'README.md')
    stats_path = os.path.join(repo_root, 'stats.json')

    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    topics_map = parse_topics_from_readme(readme_content)

    stats_data = {}
    if os.path.exists(stats_path):
        try:
            with open(stats_path, 'r', encoding='utf-8') as f:
                stats_data = json.load(f)
        except Exception as e:
            print(f"Error loading stats.json: {e}")

    shas = stats_data.get('leetcode', {}).get('shas', {})

    problem_dirs = []
    for item in os.listdir(repo_root):
        item_path = os.path.join(repo_root, item)
        if os.path.isdir(item_path) and re.match(r'^\d{4}-', item):
            problem_dirs.append(item)

    problem_dirs.sort()

    problems = []
    easy_count = 0
    med_count = 0
    hard_count = 0

    for pdir in problem_dirs:
        pdir_path = os.path.join(repo_root, pdir)
        prob_num_match = re.match(r'^(\d{4})-(.*)$', pdir)
        if not prob_num_match:
            continue
        prob_num = prob_num_match.group(1)
        prob_slug = prob_num_match.group(2)

        prob_readme = os.path.join(pdir_path, 'README.md')
        prob_title = prob_slug.replace('-', ' ').title()
        prob_url = f"https://leetcode.com/problems/{prob_slug}/"
        prob_diff = "Easy"

        if pdir in shas and 'difficulty' in shas[pdir]:
            prob_diff = shas[pdir]['difficulty'].capitalize()

        if os.path.exists(prob_readme):
            try:
                with open(prob_readme, 'r', encoding='utf-8') as pf:
                    ptext = pf.read()
                    h2_match = re.search(r'<h2><a\s+href="([^"]+)">([^<]+)</a></h2>(?:\s*<h3>([^<]+)</h3>)?', ptext)
                    if h2_match:
                        prob_url = h2_match.group(1)
                        full_title = h2_match.group(2).strip()
                        prob_title = re.sub(r'^\d+\.\s*', '', full_title)
                        if h2_match.group(3):
                            prob_diff = h2_match.group(3).strip().capitalize()
            except Exception as e:
                print(f"Error reading {prob_readme}: {e}")

        diff_lower = prob_diff.lower()
        if diff_lower == 'easy':
            easy_count += 1
        elif diff_lower == 'medium':
            med_count += 1
        elif diff_lower == 'hard':
            hard_count += 1

        # Find solution code files
        code_files = []
        for file in os.listdir(pdir_path):
            if file != 'README.md' and os.path.isfile(os.path.join(pdir_path, file)):
                code_files.append(file)

        solution_links = []
        languages = set()
        for cfile in code_files:
            _, ext = os.path.splitext(cfile)
            lang = get_language_name(ext)
            languages.add(f"`{lang}`")
            solution_links.append(f"[{cfile}](./{pdir}/{cfile})")

        solution_str = ", ".join(solution_links) if solution_links else f"[{pdir}](./{pdir})"
        lang_str = ", ".join(sorted(languages)) if languages else "`C++`"

        # Topics mapping
        p_topics = set()
        for key in [pdir, prob_slug, prob_num, pdir.lower(), prob_slug.lower()]:
            if key in topics_map:
                p_topics.update(topics_map[key])
        
        # Clean topic strings
        topics_cleaned = sorted([t.replace('##', '').replace('#', '').replace('🔹', '').strip() for t in p_topics if t.strip()])
        topics_str = ", ".join([f"`{t}`" for t in topics_cleaned]) if topics_cleaned else "`Algorithms`"

        problems.append({
            'num': prob_num,
            'title': prob_title,
            'url': prob_url,
            'diff': prob_diff,
            'solution': solution_str,
            'lang': lang_str,
            'topics': topics_str
        })

    # Build Metrics Table
    total_solved = len(problems)
    metrics_table = f"""| Metric | Details |
| :--- | :--- |
| **Primary Language** | `C++ (Modern C++20)` / `C` |
| **🟢 Easy Solved** | **{easy_count}** |
| **🟡 Medium Solved** | **{med_count}** |
| **🔴 Hard Solved** | **{hard_count}** |
| **📈 Total Solved** | **{total_solved}** |
| **🔄 Auto-sync** | Powered by [LeetHub v3](https://github.com/arunbhardwaj/LeetHub-3.0) & GitHub Actions |"""

    # Build Problem Table
    table_rows = [
        "| # | Problem Title | Difficulty | Solution | Language | Topics |",
        "| :---: | :--- | :---: | :---: | :---: | :--- |"
    ]
    for p in problems:
        badge = get_difficulty_badge(p['diff'])
        row = f"| {p['num']} | [{p['title']}]({p['url']}) | {badge} | {p['solution']} | {p['lang']} | {p['topics']} |"
        table_rows.append(row)

    problems_table = "\n".join(table_rows)

    # Update README metrics section
    readme_content = re.sub(
        r'(## 📊 Progress & Metrics\n\n).*?(\n\n---)',
        r'\g<1>' + metrics_table + r'\2',
        readme_content,
        flags=re.DOTALL
    )

    # Update README problems index section
    readme_content = re.sub(
        r'(## 🧩 Problem Solutions Index\n\n).*?(\n\n---)',
        r'\g<1>' + problems_table + r'\2',
        readme_content,
        flags=re.DOTALL
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Successfully updated README.md with {total_solved} problems ({easy_count} Easy, {med_count} Medium, {hard_count} Hard).")

if __name__ == '__main__':
    main()

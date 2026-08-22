import os
import re
import json
import sys
import urllib.request

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

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
        '.cc': 'C++',
        '.cxx': 'C++',
        '.c': 'C',
        '.py': 'Python',
        '.java': 'Java',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust',
        '.cs': 'C#',
        '.kt': 'Kotlin',
        '.swift': 'Swift'
    }
    return ext_map.get(ext.lower(), ext[1:].upper() if ext.startswith('.') else ext)

def fetch_leetcode_data(slug, timeout=5):
    """Fetch problem title, difficulty, and topic tags from LeetCode GraphQL API."""
    url = "https://leetcode.com/graphql"
    query = """
    query getQuestionDetail($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            questionFrontendId
            title
            difficulty
            topicTags {
                name
                slug
            }
        }
    }
    """
    payload = json.dumps({"query": query, "variables": {"titleSlug": slug}}).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            data = json.loads(response.read().decode('utf-8'))
            return data.get('data', {}).get('question')
    except Exception as e:
        print(f"Note: Could not query LeetCode API for '{slug}': {e}")
        return None

def main():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    readme_path = os.path.join(repo_root, 'README.md')
    stats_path = os.path.join(repo_root, 'stats.json')
    cache_path = os.path.join(repo_root, 'scripts', 'topics_cache.json')

    if not os.path.exists(readme_path):
        print("README.md not found.")
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()

    # Load cache if available
    topics_cache = {}
    if os.path.exists(cache_path):
        try:
            with open(cache_path, 'r', encoding='utf-8') as cf:
                topics_cache = json.load(cf)
        except Exception as e:
            print(f"Warning: Could not read {cache_path}: {e}")

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
        if os.path.isdir(item_path) and re.match(r'^\d+-', item):
            problem_dirs.append(item)

    problem_dirs.sort()

    problems = []
    easy_count = 0
    med_count = 0
    hard_count = 0
    all_raw_langs = set()
    cache_updated = False

    for pdir in problem_dirs:
        pdir_path = os.path.join(repo_root, pdir)
        prob_match = re.match(r'^(\d+)-(.*)$', pdir)
        if not prob_match:
            continue
        prob_num = prob_match.group(1)
        prob_slug = prob_match.group(2)

        prob_readme = os.path.join(pdir_path, 'README.md')
        prob_title = prob_slug.replace('-', ' ').title()
        prob_url = f"https://leetcode.com/problems/{prob_slug}/"
        prob_diff = "Easy"
        prob_topics = []

        # Check stats.json for difficulty
        if pdir in shas and 'difficulty' in shas[pdir]:
            prob_diff = shas[pdir]['difficulty'].capitalize()

        # Check local folder README.md
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

        # Fetch/retrieve topics from cache or LeetCode GraphQL
        if prob_slug in topics_cache and topics_cache[prob_slug].get('topics'):
            cached_item = topics_cache[prob_slug]
            prob_topics = cached_item.get('topics', [])
            if cached_item.get('title'):
                prob_title = cached_item['title']
            if cached_item.get('difficulty'):
                prob_diff = cached_item['difficulty'].capitalize()
        else:
            api_data = fetch_leetcode_data(prob_slug)
            if api_data:
                prob_title = api_data.get('title', prob_title)
                prob_diff = api_data.get('difficulty', prob_diff).capitalize()
                prob_topics = [t['name'] for t in api_data.get('topicTags', [])]
                topics_cache[prob_slug] = {
                    'title': prob_title,
                    'difficulty': prob_diff,
                    'topics': prob_topics
                }
                cache_updated = True

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
        raw_langs = set()
        for cfile in code_files:
            _, ext = os.path.splitext(cfile)
            lang = get_language_name(ext)
            languages.add(f"`{lang}`")
            raw_langs.add(lang)
            all_raw_langs.add(lang)
            solution_links.append(f"[{cfile}](./{pdir}/{cfile})")

        solution_str = ", ".join(solution_links) if solution_links else f"[{pdir}](./{pdir})"
        lang_str = ", ".join(sorted(languages)) if languages else "`C++`"

        topics_cleaned = sorted([t.strip() for t in prob_topics if t.strip()])
        topics_str = ", ".join([f"`{t}`" for t in topics_cleaned]) if topics_cleaned else "`Algorithms`"

        problems.append({
            'dir': pdir,
            'num': prob_num,
            'title': prob_title,
            'url': prob_url,
            'diff': prob_diff,
            'solution': solution_str,
            'lang': lang_str,
            'raw_langs': raw_langs,
            'topics': topics_str,
            'topics_list': topics_cleaned or ['Algorithms']
        })

    # Save cache if updated
    if cache_updated:
        try:
            with open(cache_path, 'w', encoding='utf-8') as cf:
                json.dump(topics_cache, cf, indent=2, ensure_ascii=False)
            print(f"Updated topics cache in {cache_path}")
        except Exception as e:
            print(f"Warning: Could not save {cache_path}: {e}")

    # Build Primary Language string dynamically
    if 'C++' in all_raw_langs and 'C' in all_raw_langs:
        primary_lang_str = "`C++ (Modern C++20)` / `C`"
    elif 'C++' in all_raw_langs:
        primary_lang_str = "`C++ (Modern C++20)`"
    elif 'C' in all_raw_langs:
        primary_lang_str = "`C (C17)`"
    elif all_raw_langs:
        primary_lang_str = " / ".join([f"`{l}`" for l in sorted(all_raw_langs)])
    else:
        primary_lang_str = "`C++ (Modern C++20)` / `C`"

    # Build Metrics Table dynamically
    total_solved = len(problems)
    metrics_table = f"""| Metric | Details |
| :--- | :--- |
| **Primary Language** | {primary_lang_str} |
| **🟢 Easy Solved** | **{easy_count}** |
| **🟡 Medium Solved** | **{med_count}** |
| **🔴 Hard Solved** | **{hard_count}** |
| **📈 Total Solved** | **{total_solved}** |
| **🔄 Auto-sync** | Powered by [LeetHub v3](https://github.com/arunbhardwaj/LeetHub-3.0) & GitHub Actions |"""

    # Build Problem Solutions Index Table dynamically
    table_rows = [
        "| # | Problem Title | Difficulty | Solution | Language | Topics |",
        "| :---: | :--- | :---: | :---: | :---: | :--- |"
    ]
    for p in problems:
        badge = get_difficulty_badge(p['diff'])
        row = f"| {p['num']} | [{p['title']}]({p['url']}) | {badge} | {p['solution']} | {p['lang']} | {p['topics']} |"
        table_rows.append(row)

    problems_table = "\n".join(table_rows)

    # Build Categorized by Topics dynamically
    topic_map = {}
    for p in problems:
        for t in p['topics_list']:
            if t not in topic_map:
                topic_map[t] = []
            topic_map[t].append(p)

    topic_sections = []
    for topic_name in sorted(topic_map.keys()):
        topic_sections.append(f"### 🔹 {topic_name}")
        # Sort problems under topic by problem number
        sorted_topic_probs = sorted(topic_map[topic_name], key=lambda x: x['num'])
        for p in sorted_topic_probs:
            topic_sections.append(f"- [{p['num']} - {p['title']}](./{p['dir']})")
        topic_sections.append("")

    topics_body = "\n".join(topic_sections).strip()
    topics_block = f"<!---LeetCode Topics Start-->\n{topics_body}\n<!---LeetCode Topics End-->"

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

    # Update README categorized by topics section dynamically
    if '<!---LeetCode Topics Start-->' in readme_content and '<!---LeetCode Topics End-->' in readme_content:
        readme_content = re.sub(
            r'<!---LeetCode Topics Start-->.*?<!---LeetCode Topics End-->',
            topics_block,
            readme_content,
            flags=re.DOTALL
        )
    else:
        readme_content = re.sub(
            r'(## 🏷️ Categorized by Topics\n\n).*?(\n\n---)',
            r'\g<1>' + topics_block + r'\2',
            readme_content,
            flags=re.DOTALL
        )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Successfully updated README.md with {total_solved} problems ({easy_count} Easy, {med_count} Medium, {hard_count} Hard).")
    print(f"Categorized into {len(topic_map)} dynamic topics.")

if __name__ == '__main__':
    main()

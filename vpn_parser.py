import os
import sys
import base64
import requests

SOURCE_URL = [
    "https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt",
    "https://raw.githubusercontent.com/zieng2/wl/main/vless_universal.txt",
]
WORDS = ["🇷🇺", "White list", "Russia", "Россия", "RU"]

def get_source_urls():
    argv_urls = [arg.strip() for arg in sys.argv[1:] if arg.strip()]
    if argv_urls:
        return argv_urls

    env_urls = [item.strip() for item in os.environ.get("VPN_SOURCE_URLS", "").split(",") if item.strip()]
    if env_urls:
        return env_urls

    if isinstance(SOURCE_URL, (list, tuple, set)):
        return [str(url).strip() for url in SOURCE_URL if str(url).strip()]
    return [str(SOURCE_URL).strip()]

try:
        source_urls = get_source_urls()
        print(f"Используем источники: {source_urls}")

        for source_url in source_urls:
            response = requests.get(source_url)
            raw_data = response.text.strip()

            try:
                decoded_data = base64.b64decode(raw_data).decode('utf-8')
                is_base64 = True
            except Exception:
                decoded_data = raw_data
                is_base64 = False
                                                                
            all_nodes = [line for line in decoded_data.splitlines() if line.strip()]

            filtered_nodes = []
            filtered_nodes.append("""#profile-title: list.txt White List
#profile-update-interval: 1
#support-url: https://t.me/twen_two
#profile-web-page-url: https://github.com
#announce: t.me/twen_two · WhiteList configs · \n""")
            for line in all_nodes:
                if any(word in line for word in WORDS):
                    filtered_nodes.append(line)
            
            result_text = "\n".join(filtered_nodes)

            if is_base64:
                result_text = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
                                                                                                                    
            with open("list.txt", "w") as f:
                f.write(result_text)
                                                                                                                                            
            print(f"Найдено и сохранено {len(filtered_nodes)} серверов")
except Exception as e:
        print(f"Что-то пошло не так: {e}")
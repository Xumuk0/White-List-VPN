import requests
import base64

SOURCE_URL = "https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-all.txt"

try:
        response = requests.get(SOURCE_URL)
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
                if "🇷🇺" in line or "White list" in line.lower():
                        filtered_nodes.append(line)
        
        result_text = "\n".join(filtered_nodes)

        if is_base64:
                result_text = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
                                                                                                                    
        with open("list.txt", "w") as f:
                f.write(result_text)
                                                                                                                                            
        print(f"Найдено и сохранено {len(filtered_nodes)} серверов")
except Exception as e:
        print(f"Что-то пошло не так: {e}")

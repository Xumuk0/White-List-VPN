import requests
import base64

SOURCE_URL = "https://raw.githubusercontent.com/whoahaow/rjsxrd/refs/heads/main/githubmirror/bypass/bypass-1.txt"

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
                                                                            
        limited_nodes = all_nodes[:100]
                                                                                        
        result_text = "\n".join(limited_nodes)
        if is_base64:
                result_text = base64.b64encode(result_text.encode('utf-8')).decode('utf-8')
                                                                                                                    
        with open("list_vpn.txt", "w") as f:
                f.write(result_text)
                                                                                                                                            
        print("Успешно обрезано до 100 серверов!")
except Exception as e:
        print(f"Что-то пошло не так: {e}")

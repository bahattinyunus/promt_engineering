
import os
import sys

def list_prompts(root_dir):
    prompts = []
    for root, dirs, files in os.walk(root_dir):
        if 'tools' in root or '.git' in root or 'assets' in root:
            continue
        for file in files:
            if file.endswith(".md") and file != "README.md" and file != "CONTRIBUTING.md" and file != "CODE_OF_CONDUCT.md":
                # Get category from folder name
                category = os.path.basename(root)
                full_path = os.path.join(root, file)
                prompts.append({'category': category, 'name': file, 'path': full_path})
    return prompts

def display_menu(prompts):
    print("\n--- 🤖 Prompt Engineering Yöneticisi ---")
    print(f"Toplam {len(prompts)} prompt bulundu.\n")
    
    for idx, prompt in enumerate(prompts):
        print(f"{idx + 1}. [{prompt['category']}] {prompt['name']}")
    
    print("\n0. Çıkış")
    return input("\nBir prompt seçin (Numara): ")

def show_prompt(prompt_path):
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            content = f.read()
            print("\n" + "="*50)
            print(content)
            print("="*50 + "\n")
            input("Devam etmek için Enter'a basın...")
    except Exception as e:
        print(f"Hata: {e}")

def main():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # Go up one level from tools/
    
    while True:
        prompts = list_prompts(root_dir)
        choice = display_menu(prompts)
        
        if choice == '0':
            print("Güle güle! 👋")
            break
        
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(prompts):
                show_prompt(prompts[idx]['path'])
            else:
                print("Geçersiz numara!")
        else:
            print("Lütfen bir sayı girin.")

if __name__ == "__main__":
    main()

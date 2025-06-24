import re

def remove_emoji(token):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002500-\U00002BEF"  # chinese characters
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U00010000-\U0010ffff"
        u"\u2640-\u2642" 
        u"\u2600-\u2B55"
        u"\u200d"
        u"\u23cf"
        u"\u23e9"
        u"\u231a"
        u"\ufe0f"  # dingbats
        u"\u3030"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', token)

def is_phone(token):
    return len(token) == 10 and token.startswith('09') and token.isdigit()

def process_file(input_file_path):
    in_address = False
    output_lines = []
    
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            output_lines.append("")
            in_address = False
            continue
        
        parts = stripped_line.split('\t')
        if len(parts) < 2:
            output_lines.append(stripped_line)
            continue
        
        token, label = parts[0], parts[1]
        cleaned_token = remove_emoji(token)
        
        if in_address:
            if is_phone(cleaned_token):
                in_address = False
                output_lines.append(f"{cleaned_token}\tO")
            else:
                output_lines.append(f"{cleaned_token}\tI-LOC")
        else:
            if cleaned_token.startswith("አድራሻ"):
                in_address = True
                output_lines.append(f"{cleaned_token}\tB-LOC")
            else:
                output_lines.append(f"{cleaned_token}\t{label}")
    
    return output_lines

if __name__ == "__main__":
    input_file = "conll_labeled_data.txt"
    output_lines = process_file(input_file)
    with open('final.txt','w',encoding='utf-8') as file :
        for line in output_lines:
            file.write(line)
      
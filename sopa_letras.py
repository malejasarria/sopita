import json

def get_file_content(file_path):
    with open(file_path, 'r') as f:
        lines = f.read().strip().split('\n')
    
    letter_soup = []
    words = []
    for line in lines:
        if line.strip() == "---":
            break
        letter_soup.append(line.strip().replace(" ", "").upper())
    
    words = [line.strip().replace(" ", "").upper() for line in lines[len(letter_soup) + 1:]]
    return letter_soup, words

def find_word(letter_soup, word):
    n = len(letter_soup)
    m = len(letter_soup[0])
    directions = [
        (0, 1), (1, 0), (1, 1), (1, -1),
        (0, -1), (-1, 0), (-1, -1), (-1, 1)
    ]  

    def check_direction(x, y, dx, dy):
        for i in range(len(word)):
            new_x = x + i * dx
            new_y = y + i * dy
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m or letter_soup[new_x][new_y] != word[i]:
                return False
        return True

    for i in range(n):
        for j in range(m):
            if letter_soup[i][j] == word[0]:
                for dx, dy in directions:
                    if check_direction(i, j, dx, dy):
                        return True
    return False

def find_words(letter_soup, words):
    results = {}
    for word in words:
        results[word] = find_word(letter_soup, word)
    return results

def main(file_path):
    letter_soup, words = get_file_content(file_path)
    results = find_words(letter_soup, words)

    output_path = file_path.replace('.txt', '_output.json')
    with open(output_path, 'w') as json_file:
        json.dump(results, json_file, indent=4)

    print(f"El reporte ha sido guardado en: {output_path}")

if __name__ == "__main__":
    file_path = input("Ingresa la ruta del archivo de entrada: ")
    main(file_path)


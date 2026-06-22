def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]

        unique = ""
        for ch in substring:
            if ch not in unique:
                unique += ch

        print(unique)

if __name__ == '__main__':
    string = input()
    k = int(input())
    merge_the_tools(string, k)
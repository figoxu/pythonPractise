from App import FanQie


def main():
    print("hello world")
    fanqie = FanQie()  # 实例化类
    result = fanqie.search('和七零糙汉闪婚后，她秘密暴露了')
    print(result)
    # book-id
    # 7077489747005803527
    book_id = "7077489747005803527"
    item_ids = fanqie.direct(book_id)
    out_dir = "/Users/xujianhui/mobvista/mtg/github/pythonPractise/project/fanQieNovel/output"
    for index, item_id in enumerate(item_ids):
        v = fanqie.content(item_id)
        content = v["content"]
        print(content)
        title = v["title"]
        print(title)
        out_filename = out_dir + "/" + format_number_to_string(index) +"_" + title + ".html"
        body = "<h1>" + title + "</h1>" + content
        save_string_to_file(out_filename, body)


def save_string_to_file(file_name, content):
    # 打开文件并写入内容
    with open(file_name, 'w') as file:
        file.write(content)


def format_number_to_string(number):
    # 将数字转换为字符串
    num_str = str(number)

    # 计算需要补充的零的个数
    zero_count = 3 - len(num_str)

    # 使用字符串的zfill方法在左侧补充零，使总长度为5
    formatted_str = num_str.zfill(3)

    return formatted_str


if __name__ == "__main__":
    main()

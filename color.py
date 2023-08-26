def color_change(text:str,start_color:list=[147,246,228],end_color:list=[35,176,237]):
    #分割
    text_list = []
    end_text = []
    for i in text:
        text_list.append(i)

    #合并
    for i in range(len(text)+1):
        r = int(start_color[0] + (i * (end_color[0] - start_color[0] / (len(text)+1) )))
        g = int(start_color[1] + (i * (end_color[2] - start_color[0] / (len(text)+1) )))
        b = int(start_color[2] + (i * (end_color[2] - start_color[0] / (len(text)+1) )))
        hax_color =  "#" + str(hex(r)[-2:]) + str(hex(g)[-2:]) + str(hex(b)[-2:])
        if(i != len(text)):
            end_text.append(f"<color={hax_color}>{str(text[i])}</color>")

    return "".join(end_text)
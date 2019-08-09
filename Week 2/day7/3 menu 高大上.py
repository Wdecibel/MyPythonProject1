#__author__: Han
#__date__: 2018/11/14

menu = {
    "北京":{
        "朝阳":{
            "国贸":{
                "CICC":{},
                "HP":{},
                "渣打银行":{},
                "CCTV":{},
            },
            "望京": {
                "陌陌":{},
                "奔驰":{},
                "360":{},
            },
            "三里屯": {
                "优衣库":{},
                "apple":{},
            },
        },
        "昌平":{
            "沙河":{
                "老男孩":{},
                "阿泰包子":{},
            },
            "天通苑":{
                "链家":{},
                "我爱我家":{},
            },
            "回龙观":{},
        },
        "海淀":{
            "五道口":{
                "谷歌":{},
                "网易":{},
                "Sohu":{},
                "SOGO":{},
                "快手":{},
            },
            "中关村":{
                "youku":{},
                "Iqiyi":{},
                "汽车之家":{},
                "新东方":{},
                "QQ":{},
            }
        }
    },
    "上海":{
        "浦东":{
            "陆家嘴":{
                "CICC":{},
                "高盛":{},
                "摩根":{},
            },
            "外滩":{},
        },
        "闵行":{},
        "静安":{},
    },
    "山东":{
        "济南":{

        },
        "德州":{
            "乐陵":{
                "丁坞镇":{},
                "城区":{},
            },
            "平原":{

            },
        },
        "青岛":{

        },
    },

}

current_layer = menu   #实现动态循环
parent_layers = []    #保存所有父级  最后一个元素永远都是父级

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:
        print("restart")
    if choice in current_layer:
        parent_layers.append(current_layer)  #在进入下一层之前，把当当前层（也就是下一次层父级）
        #下一次loop，当用户选择b的选择，就可以直接取列表的最后一个值出来
        current_layer = current_layer[choice]   #改成了子层
    elif choice == "b":
        if parent_layers:   #
            current_layer = parent_layers.pop() #取出列表的最后一个值，返回当前层的父级值
    elif choice == "q":
        print("无此项")
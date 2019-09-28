from gprint import gprint

if __name__ == "__main__":
    g1 = "abc\nde\nf"
    g2 = "Here is a 2nd grid\n!!!!!\n!!!!!!"
    g3 = "1\n2\n3\n4\n5"
    gprint(g1, g2, g3)

    g1 = "テスト1\ntest2\n試験3\nシロガネやま"
    g2 = "Here is a 2nd グリッド\n!!!!!\n!!!!!!"
    g3 = "1\n2\n3\n4\n5"
    gprint(g1, g2, g3, enable_east_asian_width=True)
# 來做一棵聖誕樹吧! 這顆聖誕樹中間除了葉子外還掛滿了燈泡，可以透過輸入的參數來決定聖誕樹的高度，以及中間要掛什麼以及葉子的形狀

def christmas_tree(leaf='*', ornaments="0", height=5):
    '''生成聖誕樹圖案
    Params:
        leaf(str): 聖誕樹葉子的符號，預設為 '*'
        ornaments (str): 聖誕樹裝飾品的符號，預設為 '0'
        height (int): 聖誕樹的高度（層數），預設為 5

    '''
    try:
        # 檢查 leaf 和 ornaments 是否為單一字符
        if not isinstance(leaf, str) or len(leaf) != 1:
            raise ValueError("leaf 必須為字符")
        
        if not isinstance(ornaments, str) or len(ornaments) != 1:
            raise ValueError("ornaments 必須為字符")
        
        # 檢查 height 是否為正整數
        if not isinstance(height, int) or height <= 0:
            raise ValueError("height 必須為正整數")
        
        # 開始生成聖誕樹
        for i in range(1, height + 1):

            # 計算前置空格
            spaces = " " * (height - i)  
            layer = leaf

            if i > 1:
                layer += (ornaments + leaf) * (i - 1)

            print(spaces + layer)

    except ValueError as e:
        print(f"錯誤：{e}")
    except Exception as e:
        print(f"發生未知錯誤：{e}")

if __name__ == "__main__":
    christmas_tree(leaf='*', ornaments="0", height=5)
# 在某個魔法世界中，所有的咒語都是由大括號{}，中括號[]，與小括號()組成，如果一個咒語中，括號的開頭沒有在正確的位置配上對應的結尾的話咒語就會失敗!

import pytest

def vaild_spell_brackets(brackets:str = '{{}{(())}}'):
    stack = []
    pairs = {
        ')': '(', 
        '}': '{', 
        ']': '['
        }
    
    for char in brackets:

        # 左括號入stack
        if char in "([{": 
            stack.append(char)

        # 右括號檢查配對
        elif char in ")]}":
            if not stack or stack.pop() != pairs[char]:
                return "施法失敗"
    
    return "施法成功" if not stack else "施法失敗"

#測試
@pytest.mark.parametrize("spell, expected", [
    ("()", "施法成功"),
    ("{[]}", "施法成功"),
    ("({)}", "施法失敗"),
    ("[)", "施法失敗")
])
def test_spell_cases(spell, expected):
    assert vaild_spell_brackets(spell) == expected

if __name__ == "__main__":
    pytest.main()
    
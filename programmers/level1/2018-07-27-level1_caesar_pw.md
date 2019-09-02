## 문제: 시저암호 

어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 AB는 1만큼 밀면 BC가 되고, 3만큼 밀면 DE가 됩니다. z는 1만큼 밀면 a가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.


## Java

### My Solution 
```java
class Solution {
  public String solution(String s, int n) {
      String answer = "";
      
      for (char letter: s.toCharArray()){
        if(Character.isUpperCase(letter)){
            answer+=Character.toString((char)(((letter-'A' + n)%26)+'A'));
        }else if(Character.isLowerCase(letter)){
            answer+=Character.toString((char)(((letter-'a' + n)%26)+'a'));
        }else{
            answer+=" ";
        }
      }
      
      return answer;
  }
}
```

### Best solution 
```java
   String caesar(String s, int n) {
        String result = "";
    n = n % 26;
    for (int i = 0; i < s.length(); i++) {
      char ch = s.charAt(i);
      if (Character.isLowerCase(ch)) {
        ch = (char) ((ch - 'a' + n) % 26 + 'a');
      } else if (Character.isUpperCase(ch)) {
        ch = (char) ((ch - 'A' + n) % 26 + 'A');
      }
      result += ch;
    }
        return result;
    }
```

## Python

```python
def solution(s, n):
    answer = ''
    for i,letter in enumerate(s):
        index = ord(letter)
        if letter.isupper():
            answer += chr((index-65+n)%26 + 65)
        elif letter.islower():
            answer += chr((index-97+n)%26 + 97)
        else:
            answer += ' '
            
    return answer
```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12926?language=java </bold>

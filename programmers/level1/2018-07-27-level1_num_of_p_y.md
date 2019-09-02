## 문제: 문자열 내 p와 y의 개수 

대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다. 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.

예를들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.


## Java

### My Solution 
```java
import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer=true;
        String news=s.toUpperCase();
        int countP=0, countY=0;
        for(int i=0;i<news.length();i++){
            if(news.charAt(i)=='P')
                countP++;
            if(news.charAt(i)=='Y')
                countY++;
        }  
        if(countP!=countY)
            answer=false;
        return answer;
    }
}
```

### Best solution 
```java
class Solution {
    boolean solution(String s) {
        s = s.toUpperCase();

        return s.chars().filter( e -> 'P'== e).count() == s.chars().filter( e -> 'Y'== e).count();
    }
}

```

<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12916?language=java </bold>

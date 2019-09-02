## 문제: 문자열 내림차순으로 배치하기 

문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

예를들어 s가 Zbcdefg면 gfedcbZ을 리턴한다.

## Java

### My Solution 
```java
import java.util.*;
class Solution {
  public String solution(String s) {
      String answer = "";
      String[] arr = s.split("");
      Arrays.sort(arr, Collections.reverseOrder());

    return String.join("",arr);
  }
}
```

### Best solution 
```java
import java.util.Arrays;

public class ReverseStr {
    public String reverseStr(String str){
    char[] sol = str.toCharArray();
    Arrays.sort(sol);
    return new StringBuilder(new String(sol)).reverse().toString();
    }

    // 아래는 테스트로 출력해 보기 위한 코드입니다.
    public static void main(String[] args) {
        ReverseStr rs = new ReverseStr();
        System.out.println( rs.reverseStr("Zbcdefg") );
    }
}

```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12917?language=java </bold>

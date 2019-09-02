## 문제: 서울에서 김서방 찾기 

String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

## Java

### My Solution 
```java
import java.util.*;
class Solution {
  public String solution(String[] seoul) {
      List<String> inseoul = Arrays.asList(seoul);  	
	  
      return "김서방은 " + inseoul.indexOf("Kim")+ "에 있다";
  }
}
```


<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12919?language=java </bold>

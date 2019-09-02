## 문제: 수박수박수박수박수박수? 

길이가 n이고, 수박수박수박수....와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 수박수박을 리턴하고 3이라면 수박수를 리턴하면 됩니다.

예를 들어, n 이 3이면 "수박수" 4이면 "수박수박"을 리턴한다

## Java

### My Solution 
```java
class Solution {
  public String solution(int n) {
      String answer = "";
	  String wm="수박";
      for(int i=0;i<n/2;i++)
    	answer+=wm;
  
		return n%2==0 ? (answer) : (answer+wm.substring(0,1));
  }
}
```

### Best solution 
```java

public String watermelon(int n){

        return new String(new char [n/2+1]).replace("\0", "수박").substring(0,n);
    }

```



<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12922?language=java </bold>

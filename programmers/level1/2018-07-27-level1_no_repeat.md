## 문제: 같은 숫자는 싫어 

배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다. 배열 arr에서 제거 되고 남은 수들을 return 하는 solution 함수를 완성해 주세요. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
예를들면

arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.

## Java

### My Solution 
```java
import java.util.*;

public class Solution {
	public int[] solution(int []arr) {
        int[] answer = {};
        ArrayList<Integer> list = new ArrayList<>();
        for(int i=1;i<arr.length;i++){
            if(arr[i]!=arr[i-1]) //이전 원소와 현재 원소가 다를때만 값 추가한다
                list.add(arr[i-1]);
        }
        list.add(arr[arr.length-1]);
        answer = list.stream().mapToInt(i -> i).toArray();
        return answer;
	}
}
```

### Best solution 
```java
import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> tempList = new ArrayList<Integer>();
        int preNum = 10;
        for(int num : arr) {
            if(preNum != num)
                tempList.add(num);
            preNum = num;
        }
        int[] answer = new int[tempList.size()];
        for(int i=0; i<answer.length; i++) {
            answer[i] = tempList.get(i).intValue();
        }
        return answer;
    }
}

```

<bold> source: https://programmers.co.kr/learn/courses/30/lessons/12906?language=java </bold>

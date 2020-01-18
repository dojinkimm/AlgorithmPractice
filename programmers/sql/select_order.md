## 문제: 이름이 el로 끝나는 동물 찾기
: WHERE, LIKE 사용하기

`ANIMAL_INS` 테이블은 동물 보호소에 들어온 동물의 정보를 담은 테이블입니다. `ANIMAL_INS` 테이블 구조는 다음과 같으며, `ANIMAL_ID`, `ANIMAL_TYPE`, `DATETIME`, `INTAKE_CONDITION`, `NAME`, `SEX_UPON_INTAKE`는 각각 동물의 아이디, 생물 종, 보호 시작일, 보호 시작 시 상태, 이름, 성별 및 중성화 여부를 나타냅니다.

### Table 

| NAME             | TYPE       | NULLABLE |
|------------------|------------|----------|
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |



### Direction

보호소에 들어온 동물들을 이름과 보호 시작일 순으로 조회해야 한다. 이름이 같다면 나중에 보호를 시작한 동물을 먼저 보여줘야 한

예시)

| ANIMAL_ID  | NAME         |  DATETIME           |
|------------|--------------|---------------------|
| A355753	 |	Jewel	    | 2017-08-13 13:50:00 |   
| A396810    |	Raven   	| 2016-08-22 16:13:00 |
| A410668    |	Raven   	| 2015-11-19 13:41:00 |
      

## 해설

일단, ANIMAL_INS의 ANIMAL_ID, NAME, DATETIME이 나와야 한다. 
```SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ```  
그 다음에는 NAME으로 먼저 정렬하고 그 다음에는 DATETIME으로 정렬을 한다. DATETIME은 늦은 기간이 더 먼저 와야 하기 떄문에 DESC를 붙힌다
```ORDER BY NAME, DATETIME DESC```   

## Answer

```SQL
SELECT ANIMAL_ID, NAME, DATETIME FROM ANIMAL_INS ORDER BY NAME, DATETIME DESC
```


<bold> source: https://programmers.co.kr/learn/courses/30/lessons/59403?language=mysql </bold>

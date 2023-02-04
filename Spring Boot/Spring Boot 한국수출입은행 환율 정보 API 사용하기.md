#### 개요

현재 구축하고 있는 대시보드 시스템에서 환율 정보가 필요해,
한국수출입은행에서 제공하는 환율 API를 활용해 실시간 환율 정보를 제공받아 사용해 보기로 했다.

#### 활용법

##### 1. 인증키 발급받기

한국수출입은행 Open API 제공 페이지: https://www.koreaexim.go.kr/ir/HPHKIR020M01?apino=2&viewtype=C&searchselect=&searchword=

위의 페이지로 접속하면 `Open API 인증키 발급` 탭에서 간단한 본인 인증을 하면 인증키를 발급 받을 수 있다.
발급받은 Key는 `나의 인증키 발급내역` 에서 확인 가능!

![[Spring Boot/assets/Screen Shot 2023-02-03 at 10.41.35 PM.png]]

#### 2. 요청 변수 세팅하기
우선 공통 함수를 한데 모아두기 위해 스프링 폴더 구조상으로
`src > main > utils` 라는 패키지를 신규로 생성하고 `ExchangeRateUtils` 를 작성했다

이후 아래의 세개 요청 변수를 코드상으로 초기 세팅해주면 된다

![[Screen Shot 2023-02-04 at 11.28.06 PM.png]]


```java
import java.text.NumberFormat;  
import java.text.SimpleDateFormat;  
import java.util.Date;  
import java.util.Locale;

public class ExchangeRateUtils {

private static HttpURLConnection connection;
private static BigDecimal defaultExchangeRate = BigDecimal.valueOf(1300);

public static BigDecimal getExchangeRate () {

    String authKey = <발급받은 인증키>;
    String searchDate = new SimpleDateFormat("yyyyMMdd").format(new Date());
    String dataType = "AP01";
    BigDecimal exchangeRate = null;

    ...
}
```

#### 3. API Request 보내기

```java
...
public static BigDecimal getExchangeRate () {
	...
    BufferedReader reader;
    String line;
    StringBuffer responseContent = new StringBuffer();
    JSONParser parser = new JSONParser();

    try {
        // Request URL
        URL url = new URL("https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=" + authKey + "&searchdate=" + searchDate + "&data=" + dataType);
        connection = (HttpURLConnection) url.openConnection();

        // Request 초기 세팅
        connection.setRequestMethod("GET");
        connection.setConnectTimeout(5000);
        connection.setReadTimeout(5000);

        int status = connection.getResponseCode();

        // API 호출
        // 실패했을 경우 Connection Close
        if (status > 299) {
            reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            while ((line = reader.readLine()) != null) {
                responseContent.append(line);
            }
            reader.close();
        } else { // 성공했을 경우 환율 정보 추출
            reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = reader.readLine()) != null) {
                JSONArray exchangeRateInfoList = (JSONArray) parser.parse(line);

                }
            }
            reader.close();
        }
        System.out.println(responseContent.toString());

    } catch (MalformedURLException e) {
        throw new RuntimeException(e);
    } catch (IOException e) {
        throw new RuntimeException(e);
    } catch (ParseException e) {
        throw new RuntimeException(e);
    } catch (java.text.ParseException e) {
        throw new RuntimeException(e);
    } finally {
        connection.disconnect();
    }
    
    return exchangeRate;
}
```

#### 4. 가져온 데이터 파싱하여 사용하기
```java
public static BigDecimal getExchangeRate () {
	...
        } else { // 성공했을 경우 환율 정보 추출
            reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = reader.readLine()) != null) {
                JSONArray exchangeRateInfoList = (JSONArray) parser.parse(line);

                // KRW -> USD에 대한 환율 정보 조회
                for (Object o : exchangeRateInfoList) {
                    JSONObject exchangeRateInfo = (JSONObject) o;
                    if (exchangeRateInfo.get("cur_unit").equals("USD")) {

                        // 쉼표가 포함되어 String 형태로 들어오는 데이터를 Double로 파싱하기 위한 부분
                        NumberFormat format = NumberFormat.getInstance(Locale.getDefault());
                        exchangeRate = new BigDecimal(format.parse(exchangeRateInfo.get("deal_bas_r").toString()).doubleValue());
                    }
                }
           ...
    if (exchangeRate == null) {
        exchangeRate = defaultExchangeRate; // 클래스 변수로 선언
    }

    return exchangeRate;
}
```


#### 전체 코드

```java
public static BigDecimal getExchangeRate () {

    BufferedReader reader;
    String line;
    StringBuffer responseContent = new StringBuffer();
    JSONParser parser = new JSONParser();

    String authKey = <발급받은 인증키>;
    String searchDate = new SimpleDateFormat("yyyyMMdd").format(new Date());
    String dataType = "AP01";
    BigDecimal exchangeRate = null;

    try {
        // Request URL
        URL url = new URL("https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=" + authKey + "&searchdate=" + searchDate + "&data=" + dataType);
        connection = (HttpURLConnection) url.openConnection();

        // Request 초기 세팅
        connection.setRequestMethod("GET");
        connection.setConnectTimeout(5000);
        connection.setReadTimeout(5000);

        int status = connection.getResponseCode();

        // API 호출
        // 실패했을 경우 Connection Close
        if (status > 299) {
            reader = new BufferedReader(new InputStreamReader(connection.getErrorStream()));
            while ((line = reader.readLine()) != null) {
                responseContent.append(line);
            }
            reader.close();
        } else { // 성공했을 경우 환율 정보 추출
            reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
            while ((line = reader.readLine()) != null) {
                JSONArray exchangeRateInfoList = (JSONArray) parser.parse(line);

                // KRW -> USD에 대한 환율 정보 조회
                for (Object o : exchangeRateInfoList) {
                    JSONObject exchangeRateInfo = (JSONObject) o;
                    if (exchangeRateInfo.get("cur_unit").equals("USD")) {

                        // 쉼표가 포함되어 String 형태로 들어오는 데이터를 Double로 파싱하기 위한 부분
                        NumberFormat format = NumberFormat.getInstance(Locale.getDefault());
                        exchangeRate = new BigDecimal(format.parse(exchangeRateInfo.get("deal_bas_r").toString()).doubleValue());
                    }
                }
            }
            reader.close();
        }
        System.out.println(responseContent.toString());

    } catch (MalformedURLException e) {
        throw new RuntimeException(e);
    } catch (IOException e) {
        throw new RuntimeException(e);
    } catch (ParseException e) {
        throw new RuntimeException(e);
    } catch (java.text.ParseException e) {
        throw new RuntimeException(e);
    } finally {
        connection.disconnect();
    }

    if (exchangeRate == null) {
        exchangeRate = defaultExchangeRate;
    }

    return exchangeRate;
}
```
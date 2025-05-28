import java.net.http.*;
import java.net.URI;
import java.time.Duration;
import org.json.JSONObject;

public class Main {
    public static void main(String[] args) throws Exception {
        Thread.sleep(5000);

        HttpClient client = HttpClient.newHttpClient();
        HttpRequest request = HttpRequest.newBuilder()
            .uri(new URI("http://server:80/"))
            .timeout(Duration.ofSeconds(5))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
        JSONObject json = new JSONObject(response.body());
        System.out.println(json.toString(2));
    }
}
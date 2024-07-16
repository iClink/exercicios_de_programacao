//key = 92b754057ccaf96354a3ad70
import com.google.gson.Gson;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Map;
import java.util.Scanner;

public class CoinExchange {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        // variaveis globais usadas no codigo:
        int option = 0;
        double valor = 0;
        String entrada = "";
        String saida = "";
        String key = "92b754057ccaf96354a3ad70";
        String link = "https://v6.exchangerate-api.com/v6/" + key + "/latest/";


        // checa a moeda atual
        while(option <= 0 || option > 6)
        {
            System.out.println("""
                    Insira o tipo da moeda a ser convertida:\

                    [1] -- BRL (Real Brasileiro) // [2] -- USD (Dólar Americano) // [3] -- BOB (Boliviano)\

                    [4] -- ARS (Peso Argentino)  // [5] -- CLP (Peso Chileno)    // [6] -- COP (Peso Colombiano)
                    """);

            option = scan.nextInt();

            switch (option)
            {
                case 1:
                    entrada ="BRL";
                    break;

                case 2:
                    entrada = "USD";
                    break;

                case 3:
                    entrada = "BOB";
                    break;

                case 4:
                    entrada = "ARS";
                    break;

                case 5:
                    entrada = "CLP";
                    break;

                case 6:
                    entrada = "COP";
                    break;

                default:
                    System.out.println("Entrada invalida, digite novamente\n");
                    break;
            }

        }

        // checa o valor a ser inserido
        System.out.println("\nInsira o valor a ser convertido: ");

        while(valor <= 0)
        {
            valor = scan.nextDouble();

            if(valor <= 0)
            {
                System.out.println("\nDigite um valor válido:\n");
            }
        }


        // checa a moeda a ser convertida , reseta o option para entrar no laço
        option = 0;
        while(option <= 0 || option > 6)
        {
            System.out.println("""
                    Insira o tipo da moeda a qual se converterá :\

                    [1] -- BRL (Real Brasileiro) // [2] -- USD (Dólar Americano) // [3] -- BOB (Boliviano)\

                    [4] -- ARS (Peso Argentino)  // [5] -- CLP (Peso Chileno)    // [6] -- COP (Peso Colombiano)
                    """);

            option = scan.nextInt();

            switch (option)
            {
                case 1:
                    saida ="BRL";
                    break;

                case 2:
                    saida = "USD";
                    break;

                case 3:
                    saida = "BOB";
                    break;

                case 4:
                    saida = "ARS";
                    break;

                case 5:
                    saida = "CLP";
                    break;

                case 6:
                    saida = "COP";
                    break;

                default:
                    System.out.println("Entrada invalida, digite novamente\n");
                    break;
            }

        }

        try {
            // Passo 1: Fazer a Requisição HTTP
            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(link + entrada)) // concatena o link, ja declarado, com a entrada recebida
                    .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());
            String responseBody = response.body();

            // Passo 2: Parsear o JSON com Gson
            Gson gson = new Gson();
            TaxaDeCambio taxaDeCambio = gson.fromJson(responseBody, TaxaDeCambio.class);

            // Passo 3: Realizar a Conversão e Exibir o Resultado
            if (taxaDeCambio.conversion_rates.containsKey(saida)) {
                double taxa = taxaDeCambio.conversion_rates.get(saida);
                double resultado = valor * taxa;

                System.out.printf("\n%.2f %s equivale a: %.2f %s\n", valor, entrada, resultado, saida);
            } else {
                System.out.println("Algo deu errado");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

class TaxaDeCambio {
    Map<String, Double> conversion_rates;

}

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AYD;

import org.junit.Assert;
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;
import java.util.logging.Level;

public class ConnectionFLASK {

    public static String ActiveUser = "staff@gmail.com";
    public static String Categoria = "general";
    public static String sender = "staff@gmail.com";

    public static OkHttpClient webClient = new OkHttpClient();

    public static void probarConexion(String respuesta){
        try {
            Assert.assertNotNull("El webservice no esta corriendo o no tiene conexion activa.", respuesta);
        } catch (Exception e) {
        }
    }
    
    public static void testMandarCorreo(String respuesta) {
        try {
            Assert.assertFalse("El correo del recipiente no existe.", respuesta.equalsIgnoreCase("Error"));
        } catch (Exception e) {
        }
    }

    public static void testEliminarCorreo(String respuesta) {
        Assert.assertTrue("Error eliminando el correo, el resultado del webservice no fue exitoso." + respuesta, respuesta.equalsIgnoreCase("Exito"));
    }

    public static void mandarCorreo(String sender, String receiver, String texto) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("sender", sender)
                .add("receiver", receiver)
                .add("texto", texto)
                .build();
        String r = getString("mandarCorreo", formBody);
        System.out.println("rMandarCorreo- " + r);
        testMandarCorreo(r);
    }

    public static void eliminarCorreo(String sender, String receiver, String cat, String index) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("sender", sender)
                .add("categoria", cat)
                .add("receiver", receiver)
                .add("index", index)
                .build();
        String r = getString("eliminarCorreo", formBody);
        System.out.println("eliminarCorreo- " + r);
        testEliminarCorreo(r);
    }

    public static String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://0.0.0.0:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(AYD.ConnectionFLASK.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(AYD.ConnectionFLASK.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}

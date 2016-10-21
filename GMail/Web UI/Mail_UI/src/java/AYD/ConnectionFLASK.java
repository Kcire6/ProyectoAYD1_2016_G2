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

    public static void probarConexion(String respuesta) {
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

    
        public static String setFirma(String user,String firma) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .add("firma",firma)
                .build();
        String r = getString("setFirma", formBody);
        System.out.println("rsetFirma- "+ r);
        return r;
    }
        
        public static String addFirma(String user,String firma) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .add("firma",firma)
                .build();
        setFirma(user, firma);
        String r = getString("addFirma", formBody);
        System.out.println("raddFirma- "+ r);
        return r;
    }
    
        public static ArrayList<String> getFirmas(String user) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .build();
        String r = getString("getFirmas", formBody);
        String[] firmas = r.split(",,,");
        System.out.println("rgetFirmas- "+ r);
        ArrayList<String> frm = new ArrayList<String>();
        for(int x=1; x < firmas.length;x++){
            System.out.println("----|" + firmas[x]+"|----");
            frm.add(firmas[x]);
        }
        return frm;
    }       
    public static String getDFirma(String user) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .build();
        String r = getString("getDFirma", formBody);
        System.out.println("rgetDFirma- "+ r);
        
        return r;
    }

    public static ArrayList<String> GetCategorias(String user) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("receiver", user)
                .build();
        String r = getString("GetCategorias", formBody);
        String[] aux = r.split(",,,");
        ArrayList<String> aux1 = new ArrayList<String>();
        for (int i = 0; i < aux.length; i++) {
            if (!aux[i].equals("")) {
                aux1.add(aux[i]);
            }
        }
        return aux1;
    }

    public static void addCategoria(String user, String categoria) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .add("categoria", categoria)
                .build();
        String r = getString("addCategoria", formBody);
        //System.out.println("raddCategoria- " + r);
    }

    public static ArrayList<String> getSenders(String receiver, String cat) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("receiver", receiver)
                .add("cat", cat)
                .build();
        String r = getString("getSenders", formBody);
        ArrayList<String> sends = new ArrayList<String>();
        if (!r.equals("Error")) {
            String[] aux = r.split(",");
            for (int i = 0; i < aux.length; i++) {
                if (aux[i].equals("Error")) {
                    i = aux.length;
                } else if (!aux[i].equals(" ")) {
                    sends.add(aux[i]);
                }
            }
        }
        return sends;
    }

    public static ArrayList<String> getTextosDeUnSender(String receiver, String sender, String categoria) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("receiver", receiver)
                .add("sender", sender)
                .add("categoria", categoria)
                .build();
        String r = getString("getTextosDeUnSender", formBody);
        ArrayList<String> Tsends = new ArrayList<String>();
        String[] aux = r.split(",,,");
        for (int i = 0; i < aux.length; i++) {
            if (aux[i].equals("Error3")) {
                i = aux.length;
            } else if (!aux[i].equals("")) {
                Tsends.add(aux[i]);
            }
        }

        return Tsends;
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

    public static void eliminarCategoria(String user, String categoria) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("user", user)
                .add("cat", categoria)
                .build();
        String r = getString("eliminarCategoria", formBody);
        //System.out.println("reliminarCategoria- " + r);
    }

    public static void MoveMSS(String sender, String catO, String catD, String index, String user) {
        RequestBody formBody = new FormEncodingBuilder()
                .add("sender", sender)
                .add("cat1", catO)
                .add("cat2", catD)
                .add("textoIndex", index)
                .add("user", user)
                .build();
        String r = getString("moverCorreoDeCategoria", formBody);
        //System.out.println("raddCategoria- " + r);
    }

}

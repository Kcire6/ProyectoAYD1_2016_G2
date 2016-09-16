/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AYD;

import com.squareup.okhttp.RequestBody;
import java.util.ArrayList;
import org.junit.After;
import org.junit.AfterClass;
import org.junit.Before;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Mac
 */
public class ConnectionFLASKTest {

    public ConnectionFLASKTest() {
    }

    @BeforeClass
    public static void setUpClass() {
    }

    @AfterClass
    public static void tearDownClass() {
    }

    @Before
    public void setUp() {
    }

    @After
    public void tearDown() {
    }

    /**
     * Test of getString method, of class ConnectionFLASK.
     */
    @Test
    public void testGetString() {
        System.out.println("getString");
        String metodo = "";
        RequestBody formBody = null;
        String result = ConnectionFLASK.getString(metodo, formBody);
        assertNotNull(result);
    }

    @Test
    public void testGetCategorias() {
        System.out.println("getCategorias");
        String user = "staff@gmail.com";
        ArrayList<String> resultado = ConnectionFLASK.GetCategorias(user);
        assertTrue(resultado.size() >= 1);
        assertTrue(resultado.get(0).equalsIgnoreCase("general"));
    }

    @Test
    public void testAddCategoria() {
        System.out.println("addCategoria");
        String user = "staff@gmail.com";
        String categoria = "nueva";
        ArrayList<String> resultado1 = ConnectionFLASK.GetCategorias(user);
        ConnectionFLASK.addCategoria(user, categoria);
        ArrayList<String> resultado2 = ConnectionFLASK.GetCategorias(user);
        assertEquals(resultado1.size(), resultado2.size() - 1);
    }
    
    @Test
    public void testGetSenders(){
        System.out.println("getSenders");
        ArrayList<String> resultado1 = AYD.ConnectionFLASK.getSenders("staff@gmail.com", "general");
        AYD.ConnectionFLASK.mandarCorreo("staff@gmail.com", "staff@gmail.com", "test1");
        ArrayList<String> resultado2 = AYD.ConnectionFLASK.getSenders("staff@gmail.com", "general");
        assertEquals(resultado1.size(), resultado2.size() - 1);
    }
    
    @Test
    public void testGetTextosDeUnSender(){
        System.out.println("getTextosDeUnSender");
//        AYD.ConnectionFLASK.mandarCorreo("staff@gmail.com", "staff@gmail.com", "test1");
        AYD.ConnectionFLASK.mandarCorreo("staff@gmail.com", "staff@gmail.com", "test2");
        ArrayList<String> resultados = AYD.ConnectionFLASK.getTextosDeUnSender("staff@gmail.com", "staff@gmail.com", "general");
        assertTrue(resultados.get(0).equals("test1"));
        assertTrue(resultados.get(1).equals("test2"));
    }
    
    
}

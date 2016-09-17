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
 * @author happy_000
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
     * Test of probarConexion method, of class ConnectionFLASK.
     */
    @Test
    public void testProbarConexion() {
        System.out.println("probarConexion");
        String respuesta = "";
        ConnectionFLASK.probarConexion(respuesta);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of testMandarCorreo method, of class ConnectionFLASK.
     */
    @Test
    public void testTestMandarCorreo() {
        System.out.println("testMandarCorreo");
        String respuesta = "";
        ConnectionFLASK.testMandarCorreo(respuesta);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of testEliminarCorreo method, of class ConnectionFLASK.
     */
    @Test
    public void testTestEliminarCorreo() {
        System.out.println("testEliminarCorreo");
        String respuesta = "";
        ConnectionFLASK.testEliminarCorreo(respuesta);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of mandarCorreo method, of class ConnectionFLASK.
     */
    @Test
    public void testMandarCorreo() {
        System.out.println("mandarCorreo");
        String sender = "";
        String receiver = "";
        String texto = "";
        ConnectionFLASK.mandarCorreo(sender, receiver, texto);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of eliminarCorreo method, of class ConnectionFLASK.
     */
    @Test
    public void testEliminarCorreo() {
        System.out.println("eliminarCorreo");
        String sender = "";
        String receiver = "";
        String cat = "";
        String index = "";
        ConnectionFLASK.eliminarCorreo(sender, receiver, cat, index);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of setFirma method, of class ConnectionFLASK.
     */
    @Test
    public void testSetFirma() {
        System.out.println("setFirma");
        String user = "";
        String firma = "";
        ConnectionFLASK.setFirma(user, firma);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
    }

    /**
     * Test of getString method, of class ConnectionFLASK.
     */
    @Test
    public void testGetString() {
        System.out.println("getString");
        String metodo = "";
        RequestBody formBody = null;
        String expResult = "";
        String result = ConnectionFLASK.getString(metodo, formBody);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        fail("The test case is a prototype.");
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

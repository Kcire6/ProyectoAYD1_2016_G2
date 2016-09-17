/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package AYD;

import com.squareup.okhttp.RequestBody;
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
    
}

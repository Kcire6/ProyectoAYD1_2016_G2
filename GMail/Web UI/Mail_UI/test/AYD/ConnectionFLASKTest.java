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
    
}

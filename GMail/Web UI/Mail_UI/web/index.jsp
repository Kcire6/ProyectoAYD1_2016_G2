<%-- 
    Document   : SendM
    Created on : 10-may-2015, 13:05:56
    Author     : Erick
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%
String Dfirma = "&#13;&#10;&#13;&#10;"+AYD.ConnectionFLASK.getDFirma(AYD.ConnectionFLASK.ActiveUser);
%> 
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>SEND MESSAGE</title>
        <style type="text/css">
            .form-style-9{
                max-width: 450px;
                background: #FAFAFA;
                padding: 30px;
                margin: 50px auto;
                box-shadow: 1px 1px 25px rgba(0, 0, 0, 0.35);
                border-radius: 10px;
                border: 6px solid #305A72;
            }
            .form-style-9 ul{
                padding:0;
                margin:0;
                list-style:none;
            }
            .form-style-9 ul li{
                display: block;
                margin-bottom: 10px;
                min-height: 35px;
            }
            .form-style-9 ul li  .field-style{
                box-sizing: border-box; 
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box; 
                padding: 8px;
                outline: none;
                border: 1px solid #B0CFE0;
                -webkit-transition: all 0.30s ease-in-out;
                -moz-transition: all 0.30s ease-in-out;
                -ms-transition: all 0.30s ease-in-out;
                -o-transition: all 0.30s ease-in-out;

            }.form-style-9 ul li  .field-style:focus{
                box-shadow: 0 0 5px #B0CFE0;
                border:1px solid #B0CFE0;
            }
            .form-style-9 ul li .field-split{
                width: 49%;
            }
            .form-style-9 ul li .field-full{
                width: 100%;
            }
            .form-style-9 ul li input.align-left{
                float:left;
            }
            .form-style-9 ul li input.align-right{
                float:right;
            }
            .form-style-9 ul li textarea{
                width: 100%;
                height: 100px;
            }
            .form-style-9 ul li input[type="button"], 
            .form-style-9 ul li input[type="submit"] {
                -moz-box-shadow: inset 0px 1px 0px 0px #3985B1;
                -webkit-box-shadow: inset 0px 1px 0px 0px #3985B1;
                box-shadow: inset 0px 1px 0px 0px #3985B1;
                background-color: #216288;
                border: 1px solid #17445E;
                display: inline-block;
                cursor: pointer;
                color: #FFFFFF;
                padding: 8px 18px;
                text-decoration: none;
                font: 12px Arial, Helvetica, sans-serif;
            }
            .form-style-9 ul li input[type="button"]:hover, 
            .form-style-9 ul li input[type="submit"]:hover {
                background: linear-gradient(to bottom, #2D77A2 5%, #337DA8 100%);
                background-color: #28739E;
            }
            .form-style-1 {
                margin:10px auto;
                max-width: 600px;
                padding: 20px 12px 10px 20px;
                font: 26px "Lucida Sans Unicode", "Lucida Grande", sans-serif;
            }
            .form-style-1 li {
                padding: 0;
                display: block;
                list-style: none;
                margin: 10px 0 0 0;
            }
            .form-style-1 label{
                margin:0 0 3px 0;
                padding:0px;
                display:block;
                font-weight: bold;
            }
            .form-style-1 input[type=text], 
            .form-style-1 input[type=date],
            .form-style-1 input[type=datetime],
            .form-style-1 input[type=number],
            .form-style-1 input[type=search],
            .form-style-1 input[type=time],
            .form-style-1 input[type=url],
            .form-style-1 input[type=email],
            textarea, 
            select{
                box-sizing: border-box;
                -webkit-box-sizing: border-box;
                -moz-box-sizing: border-box;
                border:1px solid #BEBEBE;
                padding: 7px;
                margin:0px;
                -webkit-transition: all 0.30s ease-in-out;
                -moz-transition: all 0.30s ease-in-out;
                -ms-transition: all 0.30s ease-in-out;
                -o-transition: all 0.30s ease-in-out;
                outline: none;  
            }
            .form-style-1 input[type=text]:focus, 
            .form-style-1 input[type=date]:focus,
            .form-style-1 input[type=datetime]:focus,
            .form-style-1 input[type=number]:focus,
            .form-style-1 input[type=search]:focus,
            .form-style-1 input[type=time]:focus,
            .form-style-1 input[type=url]:focus,
            .form-style-1 input[type=email]:focus,
            .form-style-1 textarea:focus, 
            .form-style-1 select:focus{
                -moz-box-shadow: 0 0 8px #88D5E9;
                -webkit-box-shadow: 0 0 8px #88D5E9;
                box-shadow: 0 0 8px #88D5E9;
                border: 1px solid #88D5E9;
            }
            .form-style-1 .field-divided{
                width: 49%;
            }

            .form-style-1 .field-long{
                width: 100%;
            }
            .form-style-1 .field-select{
                width: 100%;
            }
            .form-style-1 .field-textarea{
                height: 400px;
            }
            .form-style-1 input[type=submit], .form-style-1 input[type=button]{
                background: #4B99AD;
                padding: 8px 15px 8px 15px;
                border: none;
                color: #fff;
            }
            .form-style-1 input[type=submit]:hover, .form-style-1 input[type=button]:hover{
                background: #4691A4;
                box-shadow:none;
                -moz-box-shadow:none;
                -webkit-box-shadow:none;
            }
            .form-style-1 .required{
                color:red;
            }
        </style>
    </head>
    <body><form>
            <ul class="form-style-1">
                <li>
                    <h1><strong>NEW MESSAGE</strong></h1>
                </li>
            </ul>
        </form>
        <form action="SendMess" method="get" class="form-style-9">
            <ul>
                <li>
                    <input type="text" name="reci" class="field-style field-split align-left" placeholder="Email" />
                </li>
                <li>
                    <textarea name="mensaje" class="field-style" placeholder="Message"><%=Dfirma %></textarea>
                </li>
                <li>
                    <input type="submit" value="SEND MESSAGE" />
                </li>
            </ul>
        </form>
    </form>
    <form action="AccionesMS" method="get" class="form-style-9">
        <ul>
            <li>
            <tr> 
                <td>
                    <input name="boton" type="submit" value="DELETE" />
                </td> 
                <td>
                    <input name="boton" type="submit" value="FIRMAS" />
                </td> 
            </tr> 
            </li>
        </ul>
    </form>
</body>
</html>

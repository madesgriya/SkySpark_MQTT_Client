import java.sql.*;
class connect{
    public static void main(String args[]){
        try{
            Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/iotdb", "t_admin", "tealesg1");
            System.out.println("Success!!!");
            con.close();
        }
        catch(Exception e){
            System.out.println(e);
        }
    }
}
import java.io.*;
import java.net.*;
import java.util.*;

public class EchoClient {
    public static void main(String[] args) throws IOException {

        // if (args.length != 2) {
        //     System.err.println(
        //         "Usage: java EchoClient <host name> <port number>");
        //     System.exit(1);
        // }

        String hostName = "127.0.0.1";
        int portNumber = 65432;

        try (
            Socket echoSocket = new Socket(hostName, portNumber);
            PrintWriter out =
                new PrintWriter(echoSocket.getOutputStream(), true);
            BufferedReader in =
                new BufferedReader(
                    new InputStreamReader(echoSocket.getInputStream()));
            BufferedReader stdIn =
                new BufferedReader(
                    new InputStreamReader(System.in))
        ) {
            String userInput;
            while ((userInput = stdIn.readLine()) != null) {
                out.println(userInput);
                String value_=in.readLine();
                //following line print the value send from Python server
                String name = value_.getClass().getName();
                value_ = value_.replaceAll("[^0-9]+", " ");
                System.out.println(value_+" "+name);
                ArrayList<String> list=new ArrayList<>(Arrays.asList(value_.trim().split(" ")));
                name = list.getClass().getName();
                System.out.println(list+" "+name);
                int cc = Integer.parseInt(list.get(0));
                int p  = Integer.parseInt(list.get(1));
                int pp = Integer.parseInt(list.get(2));
                System.out.println(cc+" "+((Object)cc).getClass().getName()+" "+p+" "+((Object)p).getClass().getName()+" "+ pp+" "+((Object)pp).getClass().getName());
                if (userInput.equals("Over")){
                  System.out.println("Input: "+ userInput);
                  try{
                      in.close();
                      out.close();
                      echoSocket.close();
                      stdIn.close();
                    }
                    catch(IOException i)
                    {
                      System.out.println(i);
                    }
              }
         }
        }
        catch (UnknownHostException e) {
            System.err.println("Don't know about host " + hostName);
            System.exit(1);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " +
                hostName);
            System.exit(1);
        }
    }
}

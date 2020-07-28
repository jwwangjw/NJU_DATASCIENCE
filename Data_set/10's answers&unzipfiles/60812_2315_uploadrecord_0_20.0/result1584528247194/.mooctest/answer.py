import java.io.IOException;
    
    
public class Main {
        
    public static void main(String[] args) throws IOException {
        byte []stream = new byte[10000];
        byte []output = new byte[4];
        System.in.read(stream);
        short index = 0;
        short result = 0;
        byte xorand = 0x0F;
        byte xoradd = 0x30;
        while(!(stream[index]>=0x30&&stream[index]<=0x39)){
            index++;
        }
        while(stream[index]>=0x30&&stream[index]<=0x39){
            result = (short) ((result<<3) + (result<<1) + (stream[index]&xorand));
            index++;
        }
        short number = result;
        result = 0;
        byte []depth = new byte[number];
        byte []valid = new byte[number];
        depth[0] = 1;
        valid[0] = 2;
        short index1, index2;
        byte max=1;
            
        for(int i=0;i<number-1;i++){
            while(!(stream[index]>=0x30&&stream[index]<=0x39)){
                index++;
            }
            while(stream[index]>=0x30&&stream[index]<=0x39){
                result = (short) ((result<<3) + (result<<1) + (stream[index]&xorand));
                index++;
            }
            index1 = result;
            result = 0;
            while(!(stream[index]>=0x30&&stream[index]<=0x39)){
                index++;
            }
            while(stream[index]>=0x30&&stream[index]<=0x39){
                result = (short) ((result<<3) + (result<<1) + (stream[index]&xorand));
                index++;
            }
            index2 = result;
            result = 0;
            if(valid[index1]!=0){
                depth[index2] = (byte) (depth[index1]+1);
                max = (depth[index2]>max) ? (depth[index2]):max;
                valid[index1]--;
                valid[index2] = 2;
            }
        }
        if(max<10){
            output[0]=(byte) (max+xoradd);
            output[1]='\n';
            System.out.write(output, 0, 2);
        }else{
            output[0]= (byte) (max/10+xoradd);
            output[1]= (byte) (max%10+xoradd);
            output[2]='\n';
            System.out.write(output, 0, 3);
        }
    }
    
}
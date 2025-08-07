public class reversearray{
    public static void main(String[] args){
    reversearray obj=new reversearray() ;
    int [] x= {1,2,3,4,5};
    obj.revnum(x);
    System.out.println("reversed array:");
    for(int i=0;i<x.length;i++){
        System.out.print(x[i]);
    }}

public void revnum(int[] x){
    int i =0,j=x.length-1;
    while(i<j){
        int c= x[i];
        x[i++]=x[j];
        x[j--]=c;
    }
}}
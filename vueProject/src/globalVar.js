export const requestUrl="http://127.0.0.1:8000"
export const lawToRequestPerUpdate=10
export function getCharacter(num){
    var res="";
    if(num<100){
        let cnt=0;
        while(num!=0){
            if(cnt==1){
                res=change(num%10)+"十"+res;
            }else{
                res=change(num%10)+res;
            }
            num=Math.floor(num/10);
            cnt++;
        }
        return res+"条";
    }else{
        let cnt=0;
        while(num!=0){
            if(cnt==1){
                res=change(num%10)+"十"+res;
            }else if(cnt==2){
                res=change(num%10)+"百"+res;
            }
            num=Math.floor(num/10);
            cnt++;
        }
        return res+"条";
    }
}
function change(num){
    switch(num){
        case 0:return "零";
        case 1:return "一";
        case 2: return "二";
        case 3:return "三";
        case 4:return "四";
        case 5:return "五";
        case 6:return "六";
        case 7:return "七";
        case 8:return "八";
        case 9:return "九";
    }
}
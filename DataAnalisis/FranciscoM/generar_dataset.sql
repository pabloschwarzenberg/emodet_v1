use dashboard;
select id,player,session,level,action,time,timestamp,
replace(state,char(13)+char(10),' ')
from api_playerstats where timestamp>'2020-11-17 00:00:00'

import config1 as conf
import commonfunc as cf
import simpletest as s

#MEMCPU
cf.Data_preparation(conf.logfile,conf.avg,conf.memory)

#WLAN CONFIG
cf.Call_dataspecific(conf.interface_list,conf.logfile)

#UPTIME
cf.Call_uptimelist(conf.interface_list,conf.logfile)

#CHANNEL UTILISATION
cf.channel_utilisation(conf.channel_start_cmd,conf.middle,conf.channel_end_cmd,conf.fname)

#SPECIFIC PROCESS
cf.access_pro(conf.logfile,conf.process_lis,conf.vsz_start,conf.vsz_end)

#VSZ SUM AND FREE COMMAND
cf.process_sum(conf.logfile,conf.vsz_start,conf.vsz_end)

#CPU%>THRES
cf.top_cmd(conf.st,conf.ed,conf.logfile,conf.thresh)

#WIFISTATS WIFI(0/1)
cf.wifistats_call(conf.logfile,conf.wifi)

#Multiple parameters curves (kB) vs time
cf.call_cat_proc_meminfo(conf.cs,conf.ce,conf.logfile,conf.pp)

#KEY PARAMETER VALUES FOR EACH MAC ADD.
cf.console(conf.fil,conf.key)

#PID, ps command
cf.perpid(conf.logfile,conf.process_list)

#REBOOT CHECK
cf.uptime(conf.logfile)

#THROUGHPUT CALCULATION
cf.throughput(conf.thrad)

#NETWORK TOPOLOGY-NO.OF SATELLITES CONN.; NTWK TYPE
s.network(conf.nwfile)

#VISUAL NTWK TOPOLOGY
cf.picrep(conf.topo)

#THROUGHPUT GRAPHS
cf.throughputeth(conf.logfile,conf.thl)





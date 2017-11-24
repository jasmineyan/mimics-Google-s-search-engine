Lab2 PRA0101 Group07

Jianning Yan(1000461715)
Shenglin Meng (1000695517)
Zhengyan Xiao (1000627627)

Instructions to run:

Frontend:
a. public IP address of the live web server:

b. enabled Google APIs

c. benchmark setup


Benchmarking ec2-34-237-28-99.compute-1.amazonaws.com (be patient).....done


Server Software:        WSGIServer/0.1
Server Hostname:        ec2-34-237-28-99.compute-1.amazonaws.com
Server Port:            80

Document Path:          /?keywords=helloworld+foo+bar
Document Length:        1309 bytes

Concurrency Level:      60
Time taken for tests:   0.834 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      146400 bytes
HTML transferred:       130900 bytes
Requests per second:    119.90 [#/sec] (mean)
Time per request:       500.414 [ms] (mean)
Time per request:       8.340 [ms] (mean, across all concurrent requests)
Transfer rate:          171.42 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1   0.8      0       3
Processing:     4   50 124.3     18     831
Waiting:        3   49 124.4     18     830
Total:          6   51 124.8     18     833
WARNING: The median and mean for the initial connection time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%     18
  66%     19
  75%     20
  80%     20
  90%     21
  95%    421
  98%    430
  99%    833
 100%    833 (longest request)


Benchmarking ec2-34-237-28-99.compute-1.amazonaws.com (be patient)
Completed 100 requests
Completed 200 requests
Completed 300 requests
Completed 400 requests
Completed 500 requests
Completed 600 requests
Completed 700 requests
Completed 800 requests
Completed 900 requests
apr_socket_recv: Connection reset by peer (104)
Total of 981 requests completed


vstat //

procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  0      0 265096  12200 277428    0    0   188   269   92  141  2  1 93  3  0
 0  0      0 265092  12200 277460    0    0     0     0   19   19  0  0 100  0  0
 0  0      0 265092  12200 277460    0    0     0     0    8   10  0  0 100  0  0
 0  0      0 265092  12200 277460    0    0     0     0    9   12  1  0 99  0  0
 0  0      0 265092  12200 277460    0    0     0     0    8   10  0  0 100  0  0



mpstat//
02:15:47 AM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle
02:15:47 AM  all    1.83    0.27    1.02    3.01    0.00    0.02    0.26    0.00    0.00   93.59



iostat//

avg-cpu:  %user   %nice %system %iowait  %steal   %idle
           1.68    0.25    0.96    2.78    0.24   94.08

Device:            tps    kB_read/s    kB_wrtn/s    kB_read    kB_wrtn
xvdap1           13.82       150.49       229.24     188509     287156




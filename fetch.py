__author__=DGideas;

import pyfetch;
import DGStorage as DGS;
i=100;
while i<999:
	pyfetch.fetch("http://xsfw.bipt.edu.cn/fwzx/portal/xxcx/cx_jbxx_gr.jsp?yonghm=5120150"+str(i),"stuinfo.htm");
	i+=1;


import scala.io.Source

val os_version = System.getProperty("os.name");
if(os_version.toLowerCase().contains("windows")){
    val files_dir = "c://python27/tree/EttonProducts/offline/Files/";
    val dma = "c://python27/tree/EttonProducts/offline/dma.data";
    val cut = "c://python27/tree/EttonProducts/offline/cut";
  }
  else{
    val files_dir = "/home/damir/Projects/EttonProducts/offline/Files/";
    val dma = "/home/damir/Projects/EttonProducts/offline/dma.data";
    val cut = "/home/damir/Projects/EttonProducts/offline/cut";
  }
  }
for (line <- Source.fromFile(cut).getLines()){
  println(line)
}


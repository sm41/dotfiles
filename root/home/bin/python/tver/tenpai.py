from subprocess import run, CompletedProcess
from pathlib  import Path
from mytool import ctrl_string
# import analyse


class gen_tag:

  def get_metadata(self, url, down_dir, header):
    cmd_ytdlp = [
      "yt-dlp",
        "--paths",  f"home:{down_dir}",
        "--output", f"{header}",
        "--print",  "series",
        "--print",  "episode",
        "--print",  "original_url",
        "--print",  "filename",
        "--print",  "ext",
        "--print",  "id",
      url
    ]
    ddd: CompletedProcess = run(cmd_ytdlp, capture_output=True, text=True).stdout.strip()
    rxw = ddd.splitlines()
    self.series, self.episode, self.url, filename, self.ext, self.id = rxw[:6]
    self.dirname  = Path(filename).parent
    self.basename = ctrl_string.ctrl_file.zen2han(Path(filename).stem)
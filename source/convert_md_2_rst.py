# -*- coding: utf-8 -*-


"""Convert Markdown to reStructuredText extension for Sphinx Doc

Scans for '.md' files and converts them to '.rst' files using pandoc.

For use it just copy this file to your source directory and add
'convert_md_2_rst' to the 'extensions' value of your 'conf.py' file.

Ensure that the source path is in the Python sys path. For that
purpose you may add this line to 'conf.py':

sys.path.insert(0, os.path.abspath('.'))
"""

import os
import pypandoc
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import shutil

def setup(app):
    path = os.path.abspath('.') + '/source'
    for dir,subdir,files in os.walk(path):
        for file in files:
            filename = os.path.join(dir, file)
	    filename_parts = os.path.splitext(filename)
            if len(filename_parts) > 1:
                filename_ext = filename_parts[1]
                if filename_ext == '.md':
                    convert_md_2_rst_process(filename_parts[0])

def convert_md_2_rst_process(filename_root):
    filename_source = filename_root + ".md"
    filename_target = filename_root + ".rst"
    #convert_text形式
    print 'Converting', os.path.basename(filename_source), 'to', os.path.basename(filename_target)
    file_source = open(filename_source)
    lines = file_source.readlines()
    file_source.close()
    data = '\n'.join(lines)
    data = data.encode('utf-8')
    data = pypandoc.convert_text(data, 'rst', format='md')
    file_target = open(filename_target, "w")
    file_target.write(data)
    file_target.flush()
    file_target.close()
    #shutil.move(filename_target, os.path.abspath('.') + '/source/' + os.path.basename(filename_target))
    #convert_file形式
    """
    print 'Converging to other format, [rst,docx,epub,mediawiki,json,html5]'
    output = pypandoc.convert_file(filename_source, 'rst', outputfile=filename_target)
    output = pypandoc.convert_file(filename_source, 'docx', outputfile=filename_root+".docx")
    output = pypandoc.convert_file(filename_source, 'epub', outputfile=filename_root+".epub")
    output = pypandoc.convert_file(filename_source, 'mediawiki', outputfile=filename_root+".mediawiki")
    output = pypandoc.convert_file(filename_source, 'json', outputfile=filename_root+".json")
    output = pypandoc.convert_file(filename_source, 'html5', outputfile=filename_root+".html5")
    """
    #assert output == ""

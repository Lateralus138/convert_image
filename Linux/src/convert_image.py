import sys, argparse  
from pathlib import PurePath, Path
from PIL import Image
def has_transparency(img):
    if img.info.get("transparency", None) is not None:
        return True
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False
def main():
    parser = argparse.ArgumentParser(description="Image conversion using Pillow.",
                                    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--input", help="Input image file path.", type=str, required=True)
    parser.add_argument("-od", "--output-dir", help="Output image file directory path. Defaults to the input file's directory.", type=str)
    parser.add_argument("-on", "--output-name", help="Output image file name without the extension. Defaults to the input file's name.", type=str)
    parser.add_argument("-ox", "--output-extension", help="Output image file extension. Defaults to 'jpg'.", default="jpg")
    parser.add_argument("-q", "--quality", help="Percentage of quality.", type=int, default=100)
    parser.add_argument("-ms", "--max-size", help="Override decompression bomb protection to allow for large file sizes. Use only if you trust the source and at your own risk.", action='store_true')
    parser.add_argument("-it", "--ignore-transparency", help="Ignore transparency if converting to a jpg.", action='store_true')
    arguments = parser.parse_args()
    input_file = Path(arguments.input)
    if not input_file.exists():
        print("File: \"" + arguments.input + "\" does not exist.")
        sys.exit(1)
    pure_input_file = PurePath(input_file)
    output_builder = ""
    path_separator = PurePath("/")
    if not arguments.output_dir:
        output_builder += pure_input_file.parent.__str__() 
    else:
        output_dir_test = Path(arguments.output_dir)
        if not output_dir_test.exists():
            print("Output directory: \"" + arguments.output_dir + "\" does not exist.")
            sys.exit(3)
        output_builder += output_dir_test.__str__()
    if (arguments.output_extension.lower() == 'jpg') or (arguments.ignore_transparency == True):
        rgb_mode = "RGB"
    else:
        rgb_mode = "RGBA"
    if not arguments.output_name:
        output_builder += path_separator.__str__() + pure_input_file.stem.__str__()
    else:
        output_builder += path_separator.__str__() + arguments.output_name
    output_builder += "." + arguments.output_extension
    pure_output_path = PurePath(output_builder)
    if arguments.max_size == True:
         Image.MAX_IMAGE_PIXELS = None
    try :
        with Image.open(pure_input_file) as input_image:
            if not arguments.ignore_transparency:
                if ((arguments.output_extension.lower() == "jpg") and has_transparency(input_image)):
                    print("\"" + pure_input_file.__str__() + "\" has transparency and can not be converted to a jpg.")
                    sys.exit(5)
            try :
                print("Attempting to convert: \"" + pure_input_file.__str__() + "\" to file type: [" + arguments.output_extension + "]...")
                rgb_convert = input_image.convert(rgb_mode)
            except Exception as error :
                print(error)
                sys.exit(6)  
            try :
                print("Attempting to save file: \"" + pure_output_path.__str__() + "\"...")
                rgb_convert.save(pure_output_path, quality=arguments.quality)
            except Exception as error :
                print(error)
                sys.exit(7)  
            print("\"" + pure_input_file.__str__() + "\" successfully converted to:\n\"" + pure_output_path.__str__() + "\"")
    except Exception as error :
        print(error)
        sys.exit(4)
if __name__ ==  "__main__":
    main()

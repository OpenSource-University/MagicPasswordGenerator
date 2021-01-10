#include <iostream>
#include <stdio.h>
#include <stdbool.h>
#include <sys/stat.h>
#include <sstream>
#include <map>
#include <vector>
#include "scripts.h"
using namespace std;

bool symlink_exists(const char* path)
{
    struct stat buf;
    int result;
    result = lstat(path, &buf);
    return (result == 0);
}

void test(const char* path)
{
    bool exists = symlink_exists(path);
    printf("%s does%s exist.\n", path, exists ? "" : " not");
}
// =====================================
void make_checksum(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("RUN THE GENERATION OF CHECKSUM FOR "+ss1.str())){
                if (yesorno("MAKE SECTORS BY SECTORS "+ss1.str())){
                    string fcheck;
                    cout << "filelist of checksum(out): ";
                    cin >> fcheck;
                    stringstream ss2;
                    ss2 << "verify_sector_by_sector_files_checksum SET --sectors --fcheck=\""<<fcheck<<"\" --symlink=\""<<ss1.str()<<"\"";
                    system(ss2.str().c_str());
                }
                else{
                    string fcheck;
                    cout << "file of checksum(out): ";
                    cin >> fcheck;
                    stringstream ss2;
                    ss2 << "verify_sector_by_sector_files_checksum SET --fcheck=\""<<fcheck<<"\" --symlink=\""<<ss1.str()<<"\"";
                    system(ss2.str().c_str());
                }
            }
            else{
                cout << "OK ITS NOT YOUR TARGET..." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
void verif_checksum(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("RUN THE VERIFICATION OF CHECKSUM FOR "+ss1.str())){
                if (yesorno("MAKE SECTORS BY SECTORS "+ss1.str())){
                    string fcheck;
                    cout << "filelist of checksum(in): ";
                    cin >> fcheck;
                    stringstream ss2;
                    ss2 <<"verify_sector_by_sector_files_checksum GET --sectors --fcheck=\""<<fcheck<<"\" --symlink=\""<<ss1.str()<<"\"";
                    system(ss2.str().c_str());
                }
                else{
                    string fcheck;
                    cout << "file of checksum(in): ";
                    cin >> fcheck;
                    stringstream ss2;
                    ss2 << "verify_sector_by_sector_files_checksum GET --fcheck=\""<<fcheck<<"\" --symlink=\""<<ss1.str()<<"\"";
                    system(ss2.str().c_str());
                }
            }
            else{
                cout << "OK ITS NOT YOUR TARGET..." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
// =====================================
// =====================================
void choice_install(void){
    system("sudo sh install-deps-script.sh");
}
// =====================================
void choice_burnimg(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("RUN THE BURN ON "+ss1.str())){
                burn_script_sr(ss1.str());
                exit(0);
            }
            else{
                cout << "OK ITS NOT YOUR TARGET..." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
void choice_dumpcd(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("RUN THE DUMP OF "+ss1.str())){
                dump_script_sr(ss1.str());
                exit(0);
            }
            else{
                cout << "OK ITS NOT YOUR TARGET..." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
void choice_checksumcdrom(void){
    if (yesorno("GENERATE AN CHECKSUM OF AN CD-ROM ?(no: for just check an CDROM from existing checksum) ")){
        make_checksum();
    }
    else{
        verif_checksum();
    }
}
// =====================================
void choice_pwsgenerate(void){
    int nb;
    cout << "LEN OF PASSWORD: ";
    cin >> nb;
    stringstream ss1;
    ss1 << "readncut_stream GENPASSWORD -pws " << nb;
    system(ss1.str().c_str());
}
// =====================================
void choice_rkfgenerate(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("GENERATE RAWKEYSFILE IMAGE "+ss1.str())){
                string pathfile;
                cout << "FilePath: ";
                cin >> pathfile;
                stringstream ss1;
                ss1 << "dd if=/dev/urandom bs=2048 count=325000 iflag=fullblock status=progress of=" << pathfile;
                system(ss1.str().c_str());
            }
            else{
                cout << "CANCEL...OK." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
void choice_rkfburn(void){
    stringstream ss1;
    for (int i=0; i<99; i++){
        ss1 << "/dev/sr" << i;
        if (symlink_exists(ss1.str().c_str())){
            if (yesorno("GENERATE RAWKEYSFILE IMAGE AND BURN ON AN CDROM "+ss1.str())){
                string pathfile;
                cout << "FilePath: ";
                cin >> pathfile;
                string symlink;
                symlink = ss1.str();
                cout << "PLACE AN BLANK CDROM INTO THE OPTICAL DRIVE NOW. (30seconds left before close and starting)";
                system("sudo eject -T");
                system("sudo sleep 30s && sudo eject -T");
                stringstream ss1;
                ss1 << "dd if=/dev/urandom bs=2048 count=325000 iflag=fullblock status=progress of=" << pathfile;
                system(ss1.str().c_str());
                ss1.str("");
                ss1 << "sudo cdrskin -v dev=" << symlink << " -dao "<<pathfile;
                system(ss1.str().c_str());
                cout << "GET THE RAWKEYS CDROM FROM THE OPTICAL DRIVE NOW. (30seconds left before close)";
                system("sudo eject -T");
                system("sudo sleep 30s && sudo eject -T");
            }
            else{
                cout << "CANCEL...OK." << endl;
            }
        }
        ss1.str("");
    }
    cout << "NO CDROM... EXIT..." << endl;
    exit(0);
}
// =====================================
void choice_cutfullcdrom(void){
    string filepath;
    cout << "folder path for make imgs: ";
    cin >> filepath;
    string symlink;
    cout << "symlink for dump: ";
    cin >> symlink;
    int sectors_size;
    cout << "size of sectors files: ";
    cin >> sectors_size;
    stringstream ss1;
    ss1 << "readncut_stream RUN -sb=" << sectors_size <<  " -pf=\"" <<filepath <<"\" -sp=\""<< symlink<<"\"";
    if (yesorno("SPLIT WITH THIS PARAMS? SURE? AGREE ")){
        system(ss1.str().c_str());
    }
    else{
        cout << "OPERATION ABORTED."<< endl;
        exit (0);
    }
}
// =====================================
void choice_PDTSLSW(void){
    system("sudo magicpsswd");
}
// =====================================
void choice_config(void){
    system("sudo nano /var/pdtslsw/config.json");
}
// =====================================
void choice_CHECK_ENTROPY(void){
    cout << "if is under 200 you have an problem for cryptography!" << endl;
    system("cat /proc/sys/kernel/random/entropy_avail && sleep 10s");
}
// =====================================
void menu(void){
    system("sudo echo By Rick Sanchez D-634 ");
    while(true){
        system("clear");
        cout << "Welcome to the NoBrain4Passwords tools! BUILD v1.6.0" << endl;
        cout << "# ========================================================================== #" << endl;
        //cout << "(0)INSTALL DEPS & TOOLS(0)" << endl;
        cout << "(1)COPY AN IMG RAWKEYS TO CDROM WRITER DEVICE(1)" << endl;
        cout << "(2)DUMP AN CDROM RAWKEYS TO DISK(2)" << endl;
        cout << "(3)MAKE AN VERIFICATION OF AN CDROM CHECKSUM(3)" << endl;
        cout << "# ========================================================================== #" << endl;
        cout << "(4)GENERATE AN PASSWORD AND GET INTO TERMINAL(4)" << endl;
        cout << "(5)GENERATE RAWKEYS FILE IMG(5)" << endl;
        cout << "(6)GENERATE & BURN AN RAWKEYS FILE IMG(6)" << endl;
        cout << "# ========================================================================== #" << endl;
        cout << "(7)CUT TOTALY THE RAWKEYS CDROM IN SECTORS FILES(7)" << endl;
        cout << "# ========================================================================== #" << endl;
        cout << "(8)USE THE Magic Password Generator TOOL(8)" << endl;
        cout << "(9)MODIFY THE CONFIGURATION FILE(9)" << endl;
        cout << "# ========================================================================== #" << endl;
        cout << "(10)CHECK THE ENTROPY STATE(10)" << endl;
        //cout << "(11)ENTROPY MONITOR(11)" << endl;
        cout << "# ========================================================================== #" << endl;
        cout << endl;
        cout << "Choice >>";
        int choice;
        cin >> choice;
        switch (choice){
            //case 0:
            //    choice_install();
            //    break;
            case 1:
                choice_burnimg();
                break;
            case 2:
                choice_dumpcd();
                break;
            case 3:
                choice_checksumcdrom();
                break;
            case 4:
                choice_pwsgenerate();
                cout << "It's an old function you can insult is just weak...(no effect)" << endl;
                int rienadire;
                cin >> rienadire;
                break;
            case 5:
                choice_rkfgenerate();
                break;
            case 6:
                choice_rkfburn();
                break;
            case 7:
                choice_cutfullcdrom();
                break;
            case 8:
                choice_PDTSLSW();
                break;
            case 9:
                choice_config();
                break;
            case 10:
                choice_CHECK_ENTROPY();
                break;
            //case 11:
            //   entropy_monitor();
            default:
                system("clear");
        }
    };
};




int main()
{
    menu();
    return 0;
}

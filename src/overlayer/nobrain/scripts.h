#ifndef SCRIPTS_H_INCLUDED
#define SCRIPTS_H_INCLUDED
#include <iostream>
#include <sstream>
using namespace std;
// =====================================
bool yesorno(string question){
    string reply;
    while(true){
        cout << question << "[y/n]?" << " ";
        cin >> reply;
        if ((reply=="y") || (reply=="Y")){
            return true;
        };
        if ((reply=="n") || (reply=="N")){
            return false;
        };
    };
}
// =====================================
void burn_script_sr(string srname){
    if (yesorno("COPY AN IMG RAWKEYS TO CDROM ")){
        string pathfile;
        cout << "FilePath of img file(in): ";
        cin >> pathfile;
        cout << "PLACE AN BLANK CDROM INTO THE OPTICAL DRIVE NOW. (30seconds left before close and starting)";
        system("sudo eject -T");
        system("sudo sleep 30s && sudo eject -T");
        stringstream ss1;
        ss1 << "sudo cdrskin -v dev=" << srname << " -dao "<<pathfile;
        system(ss1.str().c_str());
        system("sudo eject -T");
        system("sudo sleep 30s && sudo eject -T");
    }
    else{
        cout << "CANCEL...OK." << endl;
    }
}

void dump_script_sr(string srname){
    string nameofimg;
    cout << "Name of img file(output): ";
    cin >> nameofimg;
    cout << "DUMP...";
    stringstream ss1;
    ss1 << "cat " << srname << " > " << nameofimg;
    system(ss1.str().c_str());
    cout << "OK.";
}

#endif // SCRIPTS_H_INCLUDED

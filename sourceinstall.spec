Name:		sourceinstall 
Summary:	The GNU Source Installer
Version:	2.5
Release:	%{mkrel 2}
Source0:	ftp://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/sourceinstall 
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv3+
BuildRequires:	libsrcinst-devel

%description
For an experienced user, this sofware provides a way to centralize source
installation, keep track of already installed packages and their relevant 
files, check installations for consistency, and have enhanced uninstallation.
For the novice but interested user, this software also offers a way to gain 
confidence with the command line (yes really), the file system, the traditional
UNIX commands, and of course with common source configuration and installation
procedures and options. 
The software is targeted at UNIX-like systems, and should work on recent 
UNIX-likes, with GNU/Linux as the primary target.
Please report any portability problem you should encounter. 
After completing installation of `sourceinstall' itself, the install procedure
becomes: 
   - surf the web, browse a CD or other resource
   - identify a desired source package
   - add it using the installer

%prep 
%setup -q

%build 
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean 
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755) 
%doc AUTHORS ChangeLog
%{_mandir}/man1/sourceinstall*
%{_bindir}/sourceinstall



%changelog
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.5-2mdv2010.0
+ Revision: 445165
- rebuild

* Thu Nov 06 2008 Adam Williamson <awilliamson@mandriva.org> 2.5-1mdv2009.1
+ Revision: 300350
- no info page any more
- no tcl stuff any more
- now builds against libsrcinst which has all the main buildrequires
- new release 2.5
- spec clean

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Thu Dec 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-5mdk
- Add buildRequires

* Sun Sep 18 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-4mdk
- Really fix PreReq thanks davide

* Sat Sep 17 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-3mdk
- Fix PreReq

* Fri Jul 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.4-2mdk
- Fix BuildRequires

* Wed Jul 20 2005 Marc Lijour <mlijour@mandriva.com> 0.4-1mdk
- Initial release as RPM


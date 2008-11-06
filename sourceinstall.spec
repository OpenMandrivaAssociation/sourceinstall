Name:		sourceinstall 
Summary:	The GNU Source Installer
Version:	2.5
Release:	%{mkrel 1}
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


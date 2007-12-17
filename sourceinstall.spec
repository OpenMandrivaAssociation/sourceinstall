%define name    sourceinstall
%define version 0.4
%define release %mkrel 5

Name:           %{name} 
Summary:        The GNU Source Installer
Version:        %{version} 
Release:        %release 
Source0:	ftp://ftp.gnu.org/gnu/sourceinstall/sourceinstall-0.4.tar.bz2
URL:            http://www.gnu.org/software/sourceinstall 

Group:          Development/Other
License:        GPL

BuildRequires:  expect 
BuildRequires:  tk 
BuildRequires:  tcl

Requires:       expect 
BuildRequires:  zip 
BuildRequires:  unzip 
BuildRequires:  bzip2 
BuildRequires:  ncompress 
BuildRequires:  gzip 
BuildRequires:  tar
 
Requires(post):  info-install
Requires(preun): info-install
BuildArch: 	noarch

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
%setup -q -n sourceinstall

%build 
#%configure --prefix=%{_prefix}
%configure2_5x --prefix=%{_prefix}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root,0755) 
%doc README NEWS COPYING AUTHORS 
%{_mandir}/man1/sourceinstall*
%{_infodir}/sourceinstall.info*
%{_bindir}/sourceinstall
%{_bindir}/sourceinstall.tcl

%post
# alternative way of putting this (instead of prereq)
#if [ -x /sbin/install-info ]; then
#  /sbin/install-info %{_infodir}/sourceinstall.info*
#fi
install-info %{_infodir}/sourceinstall.info*


%preun
if [ -x /sbin/install-info ]; then
  /sbin/install-info --delete %{_infodir}/sourceinstall.info*
fi

#%postun
#rm -rf %{_infodir}/sourceinstall.info*
#/sbin/install-info --delete  %{_infodir}/sourceinstall.info*


Summary:	PD Curses for DJGPP
Summary(pl):	PD Curses dla DJGPP
Name:		crossdjgpp-pdcurses
Version:	24
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	ftp://ftp.delorie.com/pub/djgpp/current/v2tk/pdcur%{version}s.zip
# Source0-md5:	3b64ba93ec3fce02dcb185f6fb5cbe5f
BuildRequires:	crossdjgpp-gcc
Requires:	crossdjgpp-gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define target i386-pc-msdosdjgpp
%define	no_install_post_strip	1


%description
PD Curses for DJGPP.

%description -l pl
PD Curses dla DJGPP.

%prep
%setup -c -T -q -n contrib/pdcur%{version}
cd ../..
unzip -a %{SOURCE0} > /dev/null

%build
mkdir obj
cp -f dos/gccdos.* obj/
cd obj
ln -sf gccdos.mak Makefile
%{__make} CC=%{target}-gcc DJDIR=$PWD/../../.. libpdcurses.a libpanel.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/%{target}/{lib,include}

install curses.h curspriv.h panel.h $RPM_BUILD_ROOT%{_prefix}/%{target}/include
install obj/libpdcurses.a obj/libpanel.a $RPM_BUILD_ROOT%{_prefix}/%{target}/lib
# convinience link
ln -sf libpdcurses.a $RPM_BUILD_ROOT%{_prefix}/%{target}/lib/libcurses.a

mv -f maintain.er MAINTAINER

# .man suffix is misleading...
for f in intro latin-1 overview x11 ; do
	gzip < doc/$f.man > $f.txt.gz
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README MAINTAINER TODO readme.*
%{_prefix}/%{target}/lib/*
%{_prefix}/%{target}/include/*

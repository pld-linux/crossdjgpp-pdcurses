Summary:	PD Curses for DJGPP
Name:		crossdjgpp-pdcurses
Version:	24
Release:	1
Epoch:		1
License:	GPL
Group:		Development/Libraries
Source0:	ftp://ftp.delorie.com/djgpp/v2misc/pdcur24s.zip
BuildRequires:	crossdjgpp-gcc
Requires:	crossdjgpp-gcc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define target i386-pc-msdosdjgpp

%description
PD Curses for DJGPP.

%prep
%setup -c -T -q -n contrib/pdcur%{version}
cd ../..
unzip -a %{SOURCE0} > /dev/null

%build
mkdir obj
cp dos/gccdos.* obj/
cd obj
ln -s gccdos.mak Makefile
make CC=%{target}-gcc DJDIR=$PWD/../../.. libpdcurses.a libpanel.a

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/%{target}/{lib,include}

install curses.h curspriv.h panel.h $RPM_BUILD_ROOT/usr/%{target}/include
install obj/libpdcurses.a obj/libpanel.a $RPM_BUILD_ROOT/usr/%{target}/lib
# convinience link
ln -s libpdcurses.a $RPM_BUILD_ROOT/usr/%{target}/lib/libcurses.a

mv maintain.er MAINTAINER
gzip -9nf README MAINTAINER TODO readme.*

# .man suffix is misleading...
for f in intro latin-1 overview x11 ; do
	gzip < doc/$f.man > $f.txt.gz
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
/usr/%{target}/lib/*
/usr/%{target}/include/*

Summary:     	Small bourne shell from Berkeley
Summary(de): 	Kleine Bourne-Shell von Berkeley
Summary(fr): 	Shell Bourne réduit de Berkeley
Summary(pl):	Ma³y shell bourne'a 
Summary(tr):	Ufak bir bourne kabuðu
Name:        	ash
Version:     	0.2
Release:     	17
Copyright:   	BSD
Group:       	Shells
Group(pl):	Pow³oki
Source:      	ftp://sunsite.unc.edu/pub/Linux/system/shells/ash-linux-%{version}.tar.gz
Patch0:       	ash-make.patch
Patch1:		ash-mknodes.patch
Prereq:      	fileutils
Prereq:		grep
Buildroot:   	/tmp/%{name}-%{version}-root
Conflicts:   	mkinitrd <= 1.7

%description
ash is a bourne shell clone from Berkeley.  It supports all of the standard
Bourne shell commands and has the advantage of supporting them while 
remaining considerably smaller than bash. 

%description -l de
ash ist ein Bourne-Shell-Clone aus Berkeley, der alle Standard-Bourne-Shell-
Befehle unterstützt und dennoch erheblich weniger Platz beansprucht als bash. 

%description -l fr
ash est un clone Berkeley du shell Bourne. Il gère toutes les commandes
standard du shell Bourne et a l'avantage de les gérer tout en restant
considérablement plus petit que bash.

%description -l pl
Ash jest klonem shell'a Bourne'a z Berkely. Obs³uguje standardowe komendy
shell'a Bourne'a i jest mniejszy ni¿ bash. 

%description -l tr
ash, Berkeley'in bir bourne kabuðu kopyasýdýr. Standart bourne kabuðu
komutlarýnýn tümünü destekler ve bash kabuðundan daha küçük olma
avantajýna sahiptir.

%prep
%setup  -q -n ash-linux-%{version}
%patch0 -p1
%patch1 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{bin,usr/man/man1}

install sh $RPM_BUILD_ROOT/bin/ash
install sh.1 $RPM_BUILD_ROOT%{_mandir}/man1/ash.1
echo ".so ash.1" > $RPM_BUILD_ROOT%{_mandir}/man1/bsh.1
ln -sf ash $RPM_BUILD_ROOT/bin/bsh

rm -f sh
make STATIC=-static

install sh $RPM_BUILD_ROOT/bin/ash.static

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%post
umask 022
echo "/bin/ash\n/bin/bsh" >> /etc/shells
cat /etc/shells | sort -u > /etc/shells.new
mv /etc/shells.new /etc/shells

%postun
if [ "$0" = 0 ]; then
	egrep -v "^/bin/ash|^/bin/bsh" /etc/shells > /etc/shells.new
	mv /etc/shells.new /etc/shells
fi

%verifyscript
for n in ash bsh; do
    echo -n "Looking for $n in /etc/shells... "
    if ! grep "^/bin/${n}\$" /etc/shells > /dev/null; then
	echo "missing"
	echo "${n} missing from /etc/shells" >&2
    else
	echo "found"
    fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /bin/*
%{_mandir}/man1/*

%changelog
* Wed Apr 21 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [0.2-17]
- added Group(pl),
- added full %defattr description,
- recompiled on rpm 3.

* Thu Mar 25 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-16]
- removed man group from man pages.

* Wed Dec 23 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-15]
- simplification in %postun and %post,
- added gzipping man pages.

* Fri Nov 06 1998 Preston Brown <pbrown@redhat.com>
  [0.2-14]
- updated to correct path on SunSITE.

* Sun Sep 27 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.2-13]
- added -q %setup parameter,
- simplification in %install,
- bsh(1) man page is now maked as nroff include to ash(1) instead
  making sym link to ash.1 (this allow compress man pages in future).

* Mon Jun 29 1998 Wojtek Slusarczyk <wojtek@shadow.eu.org>
- added pl translation.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- made /bin/ash built shared
- added ash.static
- uses a buildroot and %attr

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built against glibc
- statically linked

* Wed Apr 16 1997 Erik Troan <ewt@redhat.com>
- fixed preinstall script to >> /etc/shells for bsh.

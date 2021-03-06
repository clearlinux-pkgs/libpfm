#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpfm
Version  : 4.11.0
Release  : 6
URL      : http://sourceforge.net/projects/perfmon2/files/libpfm4/libpfm-4.11.0.tar.gz
Source0  : http://sourceforge.net/projects/perfmon2/files/libpfm4/libpfm-4.11.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: libpfm-lib = %{version}-%{release}
Requires: libpfm-license = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
libpfm4 is a library to help encode events for use with operating system
kernels performance monitoring interfaces. The current version provides support
for the perf_events interface available in upstream Linux kernels since v2.6.31.

%package dev
Summary: dev components for the libpfm package.
Group: Development
Requires: libpfm-lib = %{version}-%{release}
Provides: libpfm-devel = %{version}-%{release}
Requires: libpfm = %{version}-%{release}

%description dev
dev components for the libpfm package.


%package lib
Summary: lib components for the libpfm package.
Group: Libraries
Requires: libpfm-license = %{version}-%{release}

%description lib
lib components for the libpfm package.


%package license
Summary: license components for the libpfm package.
Group: Default

%description license
license components for the libpfm package.


%prep
%setup -q -n libpfm-4.11.0
cd %{_builddir}/libpfm-4.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599178832
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}  DBG="-g -Wall -Wextra -Wno-unused-parameter"


%install
export SOURCE_DATE_EPOCH=1599178832
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpfm
cp %{_builddir}/libpfm-4.11.0/COPYING %{buildroot}/usr/share/package-licenses/libpfm/cf50044a5e8d62462fece5fa87647aa21228b93f
cp %{_builddir}/libpfm-4.11.0/debian/copyright %{buildroot}/usr/share/package-licenses/libpfm/8b0a4692b7fac3095263d404351506c2a519a525
%make_install PREFIX=/usr LIBDIR=/usr/lib64 LDCONFIG=true

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/perfmon/perf_event.h
/usr/include/perfmon/pfmlib.h
/usr/include/perfmon/pfmlib_perf_event.h
/usr/lib64/libpfm.so
/usr/share/man/man3/libpfm.3
/usr/share/man/man3/libpfm_amd64.3
/usr/share/man/man3/libpfm_amd64_fam10h.3
/usr/share/man/man3/libpfm_amd64_fam15h.3
/usr/share/man/man3/libpfm_amd64_fam16h.3
/usr/share/man/man3/libpfm_amd64_fam17h.3
/usr/share/man/man3/libpfm_amd64_fam17h_zen2.3
/usr/share/man/man3/libpfm_amd64_k7.3
/usr/share/man/man3/libpfm_amd64_k8.3
/usr/share/man/man3/libpfm_intel_atom.3
/usr/share/man/man3/libpfm_intel_bdw.3
/usr/share/man/man3/libpfm_intel_bdx_unc_cbo.3
/usr/share/man/man3/libpfm_intel_bdx_unc_ha.3
/usr/share/man/man3/libpfm_intel_bdx_unc_imc.3
/usr/share/man/man3/libpfm_intel_bdx_unc_irp.3
/usr/share/man/man3/libpfm_intel_bdx_unc_pcu.3
/usr/share/man/man3/libpfm_intel_bdx_unc_qpi.3
/usr/share/man/man3/libpfm_intel_bdx_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_bdx_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_bdx_unc_sbo.3
/usr/share/man/man3/libpfm_intel_bdx_unc_ubo.3
/usr/share/man/man3/libpfm_intel_core.3
/usr/share/man/man3/libpfm_intel_glm.3
/usr/share/man/man3/libpfm_intel_hsw.3
/usr/share/man/man3/libpfm_intel_hswep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_hswep_unc_ha.3
/usr/share/man/man3/libpfm_intel_hswep_unc_imc.3
/usr/share/man/man3/libpfm_intel_hswep_unc_irp.3
/usr/share/man/man3/libpfm_intel_hswep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_hswep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_hswep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_hswep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_hswep_unc_sbo.3
/usr/share/man/man3/libpfm_intel_hswep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_icl.3
/usr/share/man/man3/libpfm_intel_ivb.3
/usr/share/man/man3/libpfm_intel_ivb_unc.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_ha.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_imc.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_irp.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_ivbep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_knc.3
/usr/share/man/man3/libpfm_intel_knl.3
/usr/share/man/man3/libpfm_intel_knm.3
/usr/share/man/man3/libpfm_intel_nhm.3
/usr/share/man/man3/libpfm_intel_nhm_unc.3
/usr/share/man/man3/libpfm_intel_rapl.3
/usr/share/man/man3/libpfm_intel_skl.3
/usr/share/man/man3/libpfm_intel_skx_unc_cha.3
/usr/share/man/man3/libpfm_intel_skx_unc_imc.3
/usr/share/man/man3/libpfm_intel_skx_unc_irp.3
/usr/share/man/man3/libpfm_intel_skx_unc_m2m.3
/usr/share/man/man3/libpfm_intel_skx_unc_m3upi.3
/usr/share/man/man3/libpfm_intel_skx_unc_pcu.3
/usr/share/man/man3/libpfm_intel_skx_unc_ubo.3
/usr/share/man/man3/libpfm_intel_skx_unc_upi.3
/usr/share/man/man3/libpfm_intel_slm.3
/usr/share/man/man3/libpfm_intel_snb.3
/usr/share/man/man3/libpfm_intel_snb_unc.3
/usr/share/man/man3/libpfm_intel_snbep_unc_cbo.3
/usr/share/man/man3/libpfm_intel_snbep_unc_ha.3
/usr/share/man/man3/libpfm_intel_snbep_unc_imc.3
/usr/share/man/man3/libpfm_intel_snbep_unc_pcu.3
/usr/share/man/man3/libpfm_intel_snbep_unc_qpi.3
/usr/share/man/man3/libpfm_intel_snbep_unc_r2pcie.3
/usr/share/man/man3/libpfm_intel_snbep_unc_r3qpi.3
/usr/share/man/man3/libpfm_intel_snbep_unc_ubo.3
/usr/share/man/man3/libpfm_intel_tmt.3
/usr/share/man/man3/libpfm_intel_wsm.3
/usr/share/man/man3/libpfm_intel_wsm_unc.3
/usr/share/man/man3/libpfm_intel_x86_arch.3
/usr/share/man/man3/libpfm_perf_event_raw.3
/usr/share/man/man3/pfm_find_event.3
/usr/share/man/man3/pfm_get_event_attr_info.3
/usr/share/man/man3/pfm_get_event_encoding.3
/usr/share/man/man3/pfm_get_event_info.3
/usr/share/man/man3/pfm_get_event_next.3
/usr/share/man/man3/pfm_get_os_event_encoding.3
/usr/share/man/man3/pfm_get_perf_event_encoding.3
/usr/share/man/man3/pfm_get_pmu_info.3
/usr/share/man/man3/pfm_get_version.3
/usr/share/man/man3/pfm_initialize.3
/usr/share/man/man3/pfm_strerror.3
/usr/share/man/man3/pfm_terminate.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libpfm.so.4
/usr/lib64/libpfm.so.4.10.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpfm/8b0a4692b7fac3095263d404351506c2a519a525
/usr/share/package-licenses/libpfm/cf50044a5e8d62462fece5fa87647aa21228b93f
